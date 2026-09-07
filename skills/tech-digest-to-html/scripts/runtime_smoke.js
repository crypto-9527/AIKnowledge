/**
 * AIKnowledge 运行时冒烟测试 · 最小 DOM 垫片
 * 用途：验证排版基线注入与新增主题控件后，各文档内联 JS 仍能无异常执行、无 NaN 回显。
 * 无第三方依赖，仅用 Node 内置 fs。
 */
const fs = require('fs');

function buildShim(html) {
  const REG = {};
  const ids = [...html.matchAll(/\sid="([^"]+)"/g)].map(m => m[1]);

  // 从 HTML 抽取控件初始状态（禁止手工录入，避免把页面正确逻辑误判为错误）
  const initVals = {};
  for (const m of html.matchAll(/<input\b[^>]*>/g)) {
    const tag = m[0];
    const id = (tag.match(/\sid="([^"]+)"/) || [])[1];
    if (!id) continue;
    const v = (tag.match(/\svalue="([^"]*)"/) || [])[1];
    const mn = (tag.match(/\smin="([^"]*)"/) || [])[1];
    // 浏览器原生行为：range/number 未显式给 value 时，取 min（或 0）作为初值
    if (v !== undefined) initVals[id] = v;
    else if (mn !== undefined) initVals[id] = mn;
    else if (/type="(number|range)"/.test(tag)) initVals[id] = '0';
  }
  for (const m of html.matchAll(/<select\b[^>]*\bid="([^"]+)"[^>]*>([\s\S]*?)<\/select>/g)) {
    const [, id, inner] = m;
    const sel = (inner.match(/<option[^>]*\bselected\b[^>]*\bvalue="([^"]*)"/) || [])[1];
    const first = (inner.match(/<option[^>]*\bvalue="([^"]*)"/) || [])[1];
    const v = sel !== undefined ? sel : first;
    if (v !== undefined) initVals[id] = v;
  }

  class El {
    constructor(id) {
      this.id = id; this._text = ''; this.className = ''; this.tagName = 'DIV';
      this.checked = false; this.style = {}; this.attrs = {}; this.children = [];
      this.open = false; this.disabled = false; this._h = {};
      this.value = (id in initVals) ? initVals[id] : '';
      const self = this;
      this.classList = {
        add: c => { self._cn().add(c); },
        remove: c => { self._cn().delete(c); },
        toggle: (c, f) => { const s = self._cn(); if (f === undefined) { s.has(c) ? s.delete(c) : s.add(c); } else { f ? s.add(c) : s.delete(c); } },
        contains: c => self._cn().has(c),
      };
    }
    _cn() { return this._set || (this._set = new Set()); }
    addEventListener(t, f) { (this._h[t] = this._h[t] || []).push(f); }
    removeEventListener() {}
    fire(t, ev) { (this._h[t] || []).forEach(f => f.call(this, ev || { target: this, preventDefault() {}, stopPropagation() {} })); }
    setAttribute(k, v) { this.attrs[k] = String(v); }
    getAttribute(k) { return (k in this.attrs) ? this.attrs[k] : null; }
    removeAttribute(k) { delete this.attrs[k]; }
    hasAttribute(k) { return k in this.attrs; }
    appendChild(c) { this.children.push(c); return c; }
    removeChild(c) { return c; }
    insertBefore(c) { return c; }
    closest() { return null; }
    querySelector() { return null; }
    querySelectorAll() { return []; }
    getBoundingClientRect() { return { top: 0, left: 0, right: 100, bottom: 100, width: 100, height: 100 }; }
    focus() {} blur() {} click() { this.fire('click'); }
    scrollIntoView() {} remove() {} insertAdjacentHTML() {}
    getAnimations() { return []; }
    get innerHTML() { return this._html || ''; }
    set innerHTML(v) { this._html = v; }
    get textContent() { return this._text; }
    set textContent(v) { this._text = v; }
    get parentElement() { return this._parent || (this._parent = new El('_p')); }
    get dataset() { return this._ds || (this._ds = {}); }
    get offsetWidth() { return 100; }
    get offsetHeight() { return 100; }
    get scrollHeight() { return 1000; }
    get clientHeight() { return 800; }
    get scrollTop() { return 0; }
    set scrollTop(v) {}
    get firstElementChild() { return this.children[0] || null; }
    get nextElementSibling() { return null; }
    get previousElementSibling() { return null; }
  }

  ids.forEach(id => { REG[id] = new El(id); });
  const docEl = new El('__html');
  docEl.attrs['data-theme'] = (html.match(/<html[^>]*\bdata-theme="([^"]+)"/) || [])[1] || '';
  const bodyEl = new El('__body');

  const docHandlers = {};
  const document = {
    getElementById: id => (REG[id] || (REG[id] = new El(id))),
    createElement: t => new El('_c_' + t),
    createElementNS: (ns, t) => new El('_n_' + t),
    createTextNode: t => new El('_t'),
    querySelector: () => null,
    querySelectorAll: sel => {
      if (/^#/.test(sel)) { const e = REG[sel.slice(1)]; return e ? [e] : []; }
      return [];
    },
    addEventListener: (t, f) => { (docHandlers[t] = docHandlers[t] || []).push(f); },
    removeEventListener: () => {},
    documentElement: docEl,
    body: bodyEl,
    head: new El('__head'),
    execCommand: () => true,
    title: '',
    readyState: 'complete',
  };

  const winHandlers = {};
  const window = {
    addEventListener: (t, f) => { (winHandlers[t] = winHandlers[t] || []).push(f); },
    removeEventListener: () => {},
    matchMedia: q => ({ matches: false, media: q, addEventListener() {}, addListener() {}, removeListener() {} }),
    localStorage: undefined,           // 故意留空：验证隐私模式 try/catch 分支
    print: () => {},
    scrollTo: () => {},
    scrollBy: () => {},
    requestAnimationFrame: cb => { cb(0); return 1; },
    cancelAnimationFrame: () => {},
    setTimeout: (cb) => { try { cb(); } catch (e) {} return 1; },
    getComputedStyle: () => ({ getPropertyValue: () => '' }),
    innerWidth: 1440, innerHeight: 900, scrollY: 0, pageYOffset: 0,
    location: { hash: '', href: '', pathname: '/' },
    navigator: { clipboard: undefined, userAgent: 'node' },
    document: document,
  };
  window.window = window;

  class IntersectionObserver {
    constructor(cb) { this.cb = cb; }
    observe() {} unobserve() {} disconnect() {} takeRecords() { return []; }
  }

  return { REG, document, window, docHandlers, winHandlers, IntersectionObserver, docEl, El };
}

function run(path) {
  const html = fs.readFileSync(path, 'utf8');
  const scripts = [...html.matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g)].map(m => m[1]);
  const shim = buildShim(html);
  let fatal = null;

  for (const code of scripts) {
    try {
      const fn = new Function(
        'document', 'window', 'location', 'navigator', 'IntersectionObserver',
        'requestAnimationFrame', 'cancelAnimationFrame', 'setTimeout', 'console', 'alert',
        code
      );
      fn(shim.document, shim.window, shim.window.location, shim.window.navigator,
         shim.IntersectionObserver, shim.window.requestAnimationFrame,
         shim.window.cancelAnimationFrame, shim.window.setTimeout, console, () => {});
    } catch (e) { fatal = e; break; }
  }

  // 触发 DOMContentLoaded / load / scroll，驱动初始化与进度条分支
  if (!fatal) {
    const fire = (bag, t) => (bag[t] || []).forEach(f => { try { f({ preventDefault() {}, target: shim.document.documentElement }); } catch (e) { fatal = fatal || e; } });
    fire(shim.docHandlers, 'DOMContentLoaded');
    fire(shim.docHandlers, 'readystatechange');
    fire(shim.winHandlers, 'load');
    fire(shim.winHandlers, 'scroll');
    fire(shim.winHandlers, 'resize');
  }

  // 扫描所有回显槽位
  const bad = [];
  for (const [id, el] of Object.entries(shim.REG)) {
    const t = String(el.textContent || '');
    if (/NaN|undefined|Infinity/.test(t)) bad.push(`${id} = "${t.slice(0, 60)}"`);
  }

  // 主题控件能力验证
  let theme = '-';
  if (shim.REG['aikeThemeBtn']) {
    try { shim.REG['aikeThemeBtn'].fire('click'); theme = 'click OK -> ' + shim.docEl.getAttribute('data-theme'); }
    catch (e) { theme = 'THROW: ' + e.message; fatal = fatal || e; }
  }

  const name = path.split('/').pop();
  if (fatal) {
    console.log(`FAIL  ${name}\n      ${fatal.message}`);
    return false;
  }
  console.log(`PASS  ${name}  (ids=${Object.keys(shim.REG).length}, 异常槽位=${bad.length}${theme !== '-' ? ', 主题控件=' + theme : ''})`);
  bad.slice(0, 6).forEach(b => console.log(`      ! ${b}`));
  return bad.length === 0;
}

const files = process.argv.slice(2);
let ok = true;
for (const f of files) ok = run(f) && ok;
process.exit(ok ? 0 : 1);
