// =================================================
// Olist 슬라이드 PNG export 스크립트 (Playwright)
// 사용법:
//   1. (최초 1회) npm i -D playwright && npx playwright install chromium
//   2. node export.js <input.html> <output.png>
//   3. 결과 PNG는 1920x1080 @2x = 3840x2160 (Retina)
// =================================================

const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const inputArg = process.argv[2];
  const outputArg = process.argv[3];

  if (!inputArg || !outputArg) {
    console.error('Usage: node export.js <input.html> <output.png>');
    process.exit(1);
  }

  const inputPath = path.resolve(inputArg);
  const outputPath = path.resolve(outputArg);

  const browser = await chromium.launch();
  const page = await browser.newPage({
    viewport: { width: 1920, height: 1080 },
    deviceScaleFactor: 2,           // ★ Retina export — PPT 삽입 시 선명함
  });

  await page.goto('file://' + inputPath);
  await page.waitForLoadState('networkidle');

  // 첫 번째 .slide 요소만 캡처 (한 파일에 여러 슬라이드가 있어도 첫 번째만)
  const slide = await page.locator('.slide').first();
  await slide.screenshot({ path: outputPath, omitBackground: false });

  await browser.close();
  console.log(`✓ ${outputPath} (3840x2160 @2x)`);
})();
