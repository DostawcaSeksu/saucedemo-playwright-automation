# E-Commerce Test Automation Framework

![Python](https://img.shields.io/badge/Python-3.12%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-Latest-green)
![Type](https://img.shields.io/badge/Type-UI%20%26%20Accessibility-orange)

## Overview
This project is a scalable test automation framework designed for E-commerce platforms. It demonstrates modern QA practices, including Page Object Model (POM) architecture and automated Accessibility Audits (WCAG 2.1).

The framework is built using Python and Playwright, focusing on reliability, speed, and maintainability.

## Key Features
* **Page Object Model (POM):** Clean separation between test logic and UI elements for better maintainability.
* **Strict Assertions:** Using Playwright's web-first assertions to eliminate flaky tests.
* **Accessibility Testing:** Integrated Axe-core engine to automatically detect WCAG 2.1 violations (Contrast, ARIA labels, etc.).
* **Scalable Structure:** Ready for CI/CD integration and parallel execution.

## Tech Stack
* **Language:** Python 3.12
* **Framework:** Pytest
* **Core Tool:** Playwright (UI Automation)
* **Accessibility:** Axe-Playwright
* **Version Control:** Git

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/DostawcaSeksu/saucedemo-playwright-automation
   cd saucedemo-playwright-automation
   ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

3. **Run Tests:**
    ```bash
    # Run all tests
    pytest

    # Run with visual browser (headed mode)
    pytest --headed
    ```

## Test Scenarios Covered

1.  **Authentication:** Successful login, invalid credentials handling.
2.  **Shopping Cart:** Adding items to cart, dynamic badge counter verification.
3.  **Accessibility:** Automated scan of the Login page for WCAG compliance.
