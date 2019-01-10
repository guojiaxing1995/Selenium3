Feature:
  In order to register user,
  As a tester
  I want write selenium script

  @slow
  Scenario: Open Register Page
    Given selenium driver
    When I open the register website
    Then I expect that the title is "注册"

  @wip
  Scenario Outline: Register
    """
    this is contextText
    """
    Given selenium driver
    When I input username <user_name>
    And I input password <pass_word>
    Then I except that text "成功"

    Examples:user
      | user_name        | pass_word |
      | gjx              | 123456    |
      | gjx1             | 123456    |
      | gjx2             | 123456    |
