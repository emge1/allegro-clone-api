# Test Plan – Allegro Clone

## 1. Objective
This document defines the testing approach for the  API & UI of Allegro Clone.  
The goal is to verify core functionalities such as authentication, product browsing, cart, and order processing,  
ensuring the system meets functional and non-functional requirements before release.

## 2. Scope
- **In scope:** API (REST), UI (Selenium), DB (data consistency)
- **Out of scope:** e.g., performance tests above 1000 req/s, advanced security tests

## 3. Entry Criteria
- Stable test environment
- Working endpoints and UI
- Prepared test data (JSON)

## 4. Exit Criteria
- 100% of critical tests executed
- 0 open blocker/critical defects
- Test results report available in CI
- Security and static analysis scans show no critical vulnerabilities

## 5. Types of Tests
- **Functional Tests**  
  - API tests (positive, negative, integration)  
  - UI tests (Selenium, Page Object Model, headless mode)  
  - DB tests (data consistency, transactional checks)  

- **Non-functional Tests**  
  - **Performance:** Locust tests (e.g., GET /products under 100 concurrent users)  
  - **Security Scanning:** Trivy for Docker images, Bandit for Python code  
  - **Accessibility & Usability:** Basic heuristics and automated accessibility checks  

- **Static Testing**  
  - Code linting (flake8, pylint)  
  - Type checking (mypy)  
  - Code review / pull request checks  

- **Dynamic Testing**  
  - Pytest with parametrization, markers, retry logic  
  - Parallel execution using pytest-xdist  
  - Screenshot capture on failure for UI tests  

## 6. Test Techniques
- **Black-box:** Equivalence Partitioning (EP), Boundary Value Analysis (BVA), Decision Table Testing  
- **White-box:** Statement, Branch, and Condition Coverage  
- **Experience-based:** Exploratory Testing, Error Guessing  

## 7. Tools
- **Static Analysis:** flake8, pylint, mypy, Bandit 
- **Functional Testing:** Pytest, Selenium, Requests 
- **CI/CD:** GitHub Actions, Docker
- **Reports:** JUnit, Allure (optional)
- **Management:** GitHub, Markdown
- **Performance:** Locust  
- **Security:** Trivy

## 8. Functional Scope
| Functionality        | API Endpoint            | UI         | Priority |
|----------------------|-------------------------|------------|----------|
| Login / Logout        | /login, /logout         | Login form | High     |
| Registration          | /register               | Register   | High     |
| Products              | /products, /products/id | Products   | High     |
| Cart                  | /cart                   | Cart page  | High     |
| Orders                | /customer_orders        | Orders     | High     |

## 9. Schedule
- Design: -
- Implementation: -
- Execution: -

## 10. Risks
- Unstable test environment
- Lack of test data
- Flaky tests under parallel execution 

## 11. Reporting
- CI/CD reports (HTML, JUnit)
- Defects in GitHub Issues

## 12. Team
- QA: emge1
- Dev: emge1
- DevOps: emge1
