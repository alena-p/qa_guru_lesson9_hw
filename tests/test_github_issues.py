import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser

from tests import app


def test_issue_name_pure_selene():
    browser.open("https://github.com/")
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").type("eroshenkoam/allure-example")
    browser.element(".header-search-input").submit()
    browser.element('a[href="/eroshenkoam/allure-example"]').click()
    browser.element("#issues-tab").click()
    browser.element(by.text("с днем археолога!")).should(be.visible)


def test_issue_name_lambda_steps():
    allure.dynamic.tag("issues")
    allure.dynamic.severity(Severity.CRITICAL)
    allure.dynamic.story("Все issues выводятся в разделе issues")
    allure.dynamic.feature("Issues")
    allure.dynamic.label("owner", "Potegova")
    allure.dynamic.description("Какое-то очень полезное описание как проверяется фича")
    with allure.step("Открыть главную страницу github"):
        browser.open("https://github.com/")

    with allure.step("Найти репозиторий eroshenkoam/allure-example"):
        browser.element(".header-search-input").click()
        browser.element(".header-search-input").type("eroshenkoam/allure-example")
        browser.element(".header-search-input").submit()

    with allure.step("Перейти внутрь репозитория"):
        browser.element('a[href="/eroshenkoam/allure-example"]').click()

    with allure.step("Открыть раздел issues"):
        browser.element("#issues-tab").click()

    with allure.step("Проверить, что не забыли поздравить археологов"):
        browser.element(by.text("с днем археолога!")).should(be.visible)


@allure.tag("issues")
@allure.severity(Severity.MINOR)
@allure.story("Все issues выводятся в разделе issues")
@allure.feature("Issues")
@allure.label("owner", "Potegova")
@allure.description("Какое-то очень полезное описание как проверяется фича")
def test_issue_name_decorator_steps():
    app.open_main_page()
    app.search_repo("eroshenkoam/allure-example")
    app.enter_repo("eroshenkoam/allure-example")
    app.open_issues()
    app.check_issue_present("с днем археолога!")
