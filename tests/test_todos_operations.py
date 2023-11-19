from selene import browser, have, be


def test_complete_todo():
    browser.open('/')
    registration_form = browser.element('#userForm')
    registration_form.element('#firstName').should(be.blank).type('John')
    registration_form.element('#lastName').should(be.blank).type('Week')
    registration_form.element('#userEmail').should(be.blank).type('john.week@example.com')

    registration_form.all('#genterWrapper label').element_by(have.text("Male")).click()
    # registration_form.element('//*[text()=("Male")]').click()

    registration_form.element('#userNumber').should(be.blank).type('9123456789')
    registration_form.element('#dateOfBirthInput').click()
    registration_form.element('.react-datepicker__month-dropdown-container--select').click()
    registration_form.all('.react-datepicker__month-dropdown-container--select > select').element_by(
        have.text("May")).click()
    registration_form.element('.react-datepicker__year-dropdown-container--select').click()
    registration_form.all('.react-datepicker__year-select > option').element_by(have.text("2000")).click()
    registration_form.all('.react-datepicker__day').element_by(have.text("4")).click()

    # теги
    registration_form.element('#subjectsContainer').element('.subjects-auto-complete__value-container').click()
    registration_form.element('.subjects-auto-complete__input input').set_value('Math').press_enter()

    registration_form.element('#hobbiesWrapper').element('//*[text()=("Sports")]').click()
    registration_form.element('#hobbiesWrapper').element('//*[text()=("Music")]').click()

    registration_form.element('.form-file label').click()
