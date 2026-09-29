const recordForm = document.querySelector('#record-form');
const briefForm = document.querySelector('#brief-form');

function formData(form) {
  return Object.fromEntries(new FormData(form).entries());
}

function status(id, message, kind = '') {
  const element = document.querySelector(id);
  element.textContent = message;
  element.className = `status ${kind}`;
}

async function post(path, data) {
  const response = await fetch(path, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(data),
  });
  const payload = await response.json();
  if (!response.ok) throw new Error(payload.error || `Request failed (${response.status})`);
  return payload;
}

recordForm.addEventListener('submit', async event => {
  event.preventDefault();
  const button = recordForm.querySelector('button');
  button.disabled = true;
  status('#record-status', 'Sending the resolved incident to Hindsight…');
  try {
    const payload = await post('/api/incidents', formData(recordForm));
    status('#record-status', `${payload.message} You can now brief another alert for this service.`, 'ok');
    briefForm.elements.service.value = recordForm.elements.service.value;
  } catch (error) {
    status('#record-status', error.message, 'error');
  } finally {
    button.disabled = false;
  }
});

briefForm.addEventListener('submit', async event => {
  event.preventDefault();
  const button = briefForm.querySelector('button');
  button.disabled = true;
  status('#brief-status', 'Asking Hindsight to recall relevant incidents…');
  try {
    const payload = await post('/api/brief', formData(briefForm));
    const baseline = document.querySelector('#baseline');
    const memories = document.querySelector('#memories');
    baseline.replaceChildren();
    memories.replaceChildren();
    for (const step of payload.baseline) {
      const item = document.createElement('li');
      item.textContent = step;
      baseline.append(item);
    }
    if (payload.memories.length) {
      for (const memory of payload.memories) {
        const item = document.createElement('div');
        item.className = 'memory-item';
        item.textContent = memory.text;
        memories.append(item);
      }
      status('#brief-status', `${payload.memories.length} relevant memory item(s) recalled. Review before acting.`, 'ok');
    } else {
      const empty = document.createElement('p');
      empty.className = 'no-memory';
      empty.textContent = 'No relevant prior incident was recalled. Start with the baseline checks and record the resolution afterward.';
      memories.append(empty);
      status('#brief-status', 'Hindsight found no relevant prior incident.');
    }
    document.querySelector('#bank-label').textContent = `Memory bank: ${payload.bank}`;
    document.querySelector('#brief-result').hidden = false;
    document.querySelector('#empty-prompt').hidden = true;
  } catch (error) {
    status('#brief-status', error.message, 'error');
  } finally {
    button.disabled = false;
  }
});
