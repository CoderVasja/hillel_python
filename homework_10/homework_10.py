"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import pytest

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.

    username: Ім'я користувача, яке входить в систему.

    status: Статус події входу:

    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed  - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        force=True
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)


@pytest.mark.parametrize('userName, userStatus, expected',[
    ('testUser','success','Login event - Username: testUser, Status: success'),
    ('testUser','expired','Login event - Username: testUser, Status: expired'),
    ('testUser','failed','Login event - Username: testUser, Status: failed'),
    ('testUser','invalid_status','Login event - Username: testUser, Status: invalid_status')
],
    ids=["Login Success", "Login Expired", "Login Failed", "Invalid Status"]
)
def test_log_event(userName,userStatus,expected):

    log_event(userName,userStatus)

    with open('login_system.log', 'r') as f:
        logs = f.read()
    assert expected in logs