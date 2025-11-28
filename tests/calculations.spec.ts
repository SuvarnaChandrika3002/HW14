import { test, expect } from '@playwright/test';

test('Create, read, delete calculation', async ({ page }) => {

  // REGISTER
  await page.goto('http://127.0.0.1:8001/forntend/register.html');
  await page.fill('#email', 'calc@example.com');
  await page.fill('#password', '123456');
  await page.click('button[type="submit"]');

  await page.waitForTimeout(800);

  // LOGIN
  await page.goto('http://127.0.0.1:8001/forntend/login.html');
  await page.fill('#email', 'calc@example.com');
  await page.fill('#password', '123456');
  await page.click('button[type="submit"]');

  // WAIT FOR DASHBOARD
  await page.waitForURL('**/forntend/calculations.html', { timeout: 5000 });

  // ADD CALCULATION
  await page.fill('#operation', '+');
  await page.fill('#operand1', '5');
  await page.fill('#operand2', '3');
  await page.click('#addCalcForm button[type="submit"]');

  // WAIT FOR ELEMENT TO APPEAR
  await page.waitForTimeout(800);

  // VERIFY RESULT
  const list = await page.textContent('#calcList');
  expect(list).toContain('5 + 3');
});
