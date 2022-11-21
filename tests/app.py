import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser


@allure.step("Открыть главную страницу github")
def open_main_page():
    browser.open("https://github.com/")


@allure.step("Найти репозиторий {repo_name}")
def search_repo(repo_name):
    browser.element(".header-search-input").click()
    browser.element(".header-search-input").type(repo_name)
    browser.element(".header-search-input").submit()


@allure.step("Перейти внутрь репозитория {repo_name}")
def enter_repo(repo_name):
    browser.element(f'a[href="/{repo_name}"]').click()


@allure.step("Открыть раздел issues")
def open_issues():
    browser.element("#issues-tab").click()


@allure.step("Проверить, что есть issue c именем {issue_name}")
def check_issue_present(issue_name):
    browser.element(by.text(issue_name)).should(be.visible)
