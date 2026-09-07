# 零外部依赖数学排版引擎规范 (MathML Core + 纯 CSS 优雅降级)

在零外部依赖（Zero External Dependencies）技术白皮书交付中，严禁通过 CDN 引用 KaTeX 或 MathJax（存在断网不可用、加载延迟、CDN 劫持风险），亦严禁在 HTML 中裸露未渲染的 `$$` 或 `\frac` LaTeX 源码。

本方案推荐以 **HTML5 原生 MathML Core** 为核心，结合现代 CSS 样式变量，实现零外链、高保真、完美对齐、随主题变色的终极数学排版系统。

---

## 1. 终极推荐：HTML5 原生 MathML Core (全现代浏览器内置)

自 Chromium 109（2023 年 1 月，覆盖 Chrome、Edge、Electron 及各大内置 WebView）、Safari 10+、Firefox 4+ 起，W3C MathML Core 已成为所有现代浏览器的原生 C++ 级排版标准。

### 1.1 核心排版优势
1. **彻底解决复合分式畸变**：自动处理嵌套分式（如 $\frac{1}{\frac{f}{k} + \frac{1-f}{h}}$）、运算符号（$+$、$-$、$=$）的垂直中轴对齐，绝不发生纯 CSS flexbox 下加号漂浮在分母顶部的致命 bug。
2. **公式字号自动级联（ScriptLevel）**：分式嵌套时，内层分子分母字号自动按 TeX 规范降级，避免撑爆外层。
3. **自适应根号与括号拉伸（Stretchy）**：`<msqrt>` 与伸缩括号跟随被开方数和分式高度自适应伸长，线宽与字体完美匹配。
4. **零外部网络请求**：无需加载任何第三方 JS/CSS，100% 离线自包含，完全符合自检脚本零依赖约束。

### 1.2 MathML 核心样式配置
```css
/* 数学公式容器 */
.math-block {
  margin: 1.1rem 0;
  padding: 1.1rem 1.3rem;
  background: var(--bg-subtle, #f5f5f5);
  border: 1px solid var(--border-subtle, #e0e0e0);
  border-radius: 8px;
  overflow-x: auto;
  text-align: center;
  color: var(--text-title, currentColor);
  display: flex;
  align-items: center;
  justify-content: center;
}

math {
  font-family: "Latin Modern Math", "Cambria Math", "STIX Two Math", "Newsreader", "Songti SC", Georgia, serif;
  font-size: 1.22rem;
  color: var(--text-title, currentColor);
  direction: ltr;
  line-height: 1.3;
}

math[display="block"] {
  display: block;
  margin: 0 auto;
  text-align: center;
}

math mfrac {
  padding: 0 0.15em;
}

math mo {
  padding: 0 0.18em;
}

.math-inline {
  font-family: var(--font-serif);
  font-style: italic;
  padding: 0 0.18rem;
  color: var(--text-title);
}
```

### 1.3 常用公式 MathML 模板

#### ① Amdahl 定律复合分式
```html
<div class="math-block">
  <math display="block">
    <mi>S</mi><mo stretchy="false">(</mo><mi>k</mi><mo>,</mo><mi>h</mi><mo stretchy="false">)</mo>
    <mo>=</mo>
    <mfrac>
      <mn>1</mn>
      <mrow>
        <mfrac><mi>f</mi><mi>k</mi></mfrac>
        <mo>+</mo>
        <mfrac>
          <mrow><mn>1</mn><mo>−</mo><mi>f</mi></mrow>
          <mi>h</mi>
        </mfrac>
      </mrow>
    </mfrac>
  </math>
</div>
```

#### ② USL 可扩展性定律与峰值根号
```html
<div class="math-block">
  <math display="block">
    <mi>C</mi><mo stretchy="false">(</mo><mi>N</mi><mo stretchy="false">)</mo>
    <mo>=</mo>
    <mfrac>
      <mi>N</mi>
      <mrow><mn>1</mn><mo>+</mo><mi>σ</mi><mo stretchy="false">(</mo><mi>N</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo><mo>+</mo><mi>κ</mi><mi>N</mi><mo stretchy="false">(</mo><mi>N</mi><mo>−</mo><mn>1</mn><mo stretchy="false">)</mo></mrow>
    </mfrac>
    <mspace width="2.5em"/>
    <msup><mi>N</mi><mo>*</mo></msup>
    <mo>=</mo>
    <msqrt>
      <mfrac>
        <mrow><mn>1</mn><mo>−</mo><mi>σ</mi></mrow>
        <mi>κ</mi>
      </mfrac>
    </msqrt>
  </math>
</div>
```

#### ③ 逆推对数分式
```html
<div class="math-block">
  <math display="block">
    <msup><mrow><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mi>p</mi><mo stretchy="false">)</mo></mrow><mi>n</mi></msup>
    <mo>≤</mo>
    <mi>α</mi>
    <mspace width="2em"/>
    <mo>⟹</mo>
    <mspace width="2em"/>
    <mi>n</mi>
    <mo>≥</mo>
    <mfrac>
      <mrow><mi>ln</mi><mo>&af;</mo><mi>α</mi></mrow>
      <mrow><mi>ln</mi><mo>&af;</mo><mo stretchy="false">(</mo><mn>1</mn><mo>−</mo><mi>p</mi><mo stretchy="false">)</mo></mrow>
    </mfrac>
  </math>
</div>
```

---

## 2. 纯 CSS 方案的缺陷与避坑要点 (为什么 .mfrac 容易翻车)

早期纯 CSS 手写 `.mfrac` 代码如下：
```css
.mfrac {
  display: inline-flex;
  flex-direction: column;
  vertical-align: -0.55em;
}
```
**严重缺陷分析**：
1. **Flexbox Baseline 陷阱**：对于 `display: inline-flex; flex-direction: column;`，CSS 规范强制定义其基线为第一个 flex 项目（分子 `.num`）的基线。在分母中写 `1 + <span class="mfrac">...</span>` 时，普通文本 `1 +` 会与内嵌分式的**分子**对齐，导致运算符号浮在分母顶端，产生严重的几何断裂。
2. **垂直偏移叠加**：外层声明 `vertical-align: -0.55em`，一旦嵌套，偏移量在子分式上再次叠加或产生相对行高计算错误。
3. **结论**：简单单层分式（如 $\frac{1}{1-f}$）可用 CSS `.mfrac` 快速展示，**但一旦涉及嵌套分式、带加减乘除运算符或复杂多项式，必须坚决使用 MathML Core！**

.msqrt::before {
  content: "√";
  font-size: 1.25em;
  margin-right: 1px;
  line-height: 1;
}

.msqrt > .radicand {
  border-top: 1.5px solid currentColor;
  padding-top: 0.1em;
  display: inline-block;
  line-height: 1.1;
}

/* 巨型运算符 (.msum / .mprod / .mint) */
.msum {
  display: inline-block;
  font-size: 1.4em;
  vertical-align: -0.25em;
  line-height: 1;
  font-style: normal;
}

/* 上下标 */
sup {
  font-size: 0.72em;
  vertical-align: super;
  line-height: 0;
}

sub {
  font-size: 0.72em;
  vertical-align: sub;
  line-height: 0;
}
```

---

## 2. 常用公式实现模板

### 2.1 通用可扩展性定律 (Universal Scalability Law)

公式：
$$C(N) = \frac{N}{1 + \sigma(N-1) + \kappa N(N-1)}$$

HTML 实现：
```html
<div class="math-block">
  <i>C</i>(<i>N</i>) = 
  <span class="mfrac">
    <span class="num"><i>N</i></span>
    <span class="den">1 + <i>σ</i>(<i>N</i> − 1) + <i>κ</i><i>N</i>(<i>N</i> − 1)</span>
  </span>
</div>
```

### 2.2 最优并发度拐点 (USL Peak Throughput)

公式：
$$N^* = \sqrt{\frac{1-\sigma}{\kappa}}$$

HTML 实现：
```html
<div class="math-block">
  <i>N</i><sup>*</sup> = 
  <span class="msqrt">
    <span class="radicand">
      <span class="mfrac">
        <span class="num">1 − <i>σ</i></span>
        <span class="den"><i>κ</i></span>
      </span>
    </span>
  </span>
</div>
```

### 2.3 动态排队论有效服务率与切换惩罚

公式：
$$\mu_{\text{eff}} = \frac{60}{T \cdot (1 + \gamma(N-1))}$$

HTML 实现：
```html
<div class="math-block">
  <i>μ</i><sub>eff</sub> = 
  <span class="mfrac">
    <span class="num">60</span>
    <span class="den"><i>T</i> · (1 + <i>γ</i>(<i>N</i> − 1))</span>
  </span>
</div>
```

---

## 3. 设计优势与注意事项

1. **自动适配主题**：分数线与根号上划线使用 `currentColor`，在浅色模式（如 `#181715`）与深色模式（如 `#EDEDED`）间切换时自动同步颜色，无需编写额外媒体查询。
2. **零依赖与极速加载**：无需加载 200KB+ 的 KaTeX JS/CSS 与字体包，双击即开，打印为 PDF 时矢量线条分毫毕现。
3. **标签闭合安全性**：`.mfrac` 与 `.msqrt` 内部严格使用 `<span>` 嵌套，避免任何标签错位。
