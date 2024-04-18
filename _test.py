import random

def generate_password(pw_lengths):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    passwords = []

    for length in pw_lengths:
        password = ""
        for _ in range(length):
            next_letter_index = random.randrange(len(alphabet))
            password += alphabet[next_letter_index]

        password = replace_with_number(password)
        password = replace_with_uppercase_letter(password)

        passwords.append(password)

    return passwords


def replace_with_number(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2)
        pword = pword[:replace_index] + str(random.randrange(10)) + pword[replace_index + 1:]
    return pword


def replace_with_uppercase_letter(pword):
    for _ in range(random.randrange(1, 3)):
        replace_index = random.randrange(len(pword) // 2, len(pword))
        pword = pword[:replace_index] + pword[replace_index].upper() + pword[replace_index + 1:]
    return pword


# pytest

def test_generate_password():
    pw_lengths = [4, 5, 6]
    passwords = generate_password(pw_lengths)
    assert len(passwords) == len(pw_lengths)
    for password in passwords:
        assert len(password) in pw_lengths


def test_replace_with_number():
    password = "abcd"
    new_password = replace_with_number(password)
    assert password != new_password
    assert new_password.isalnum()


def test_replace_with_uppercase_letter():
    password = "abcd"
    new_password = replace_with_uppercase_letter(password)
    assert password != new_password
    assert any(c.isupper() for c in new_password)


if __name__ == "__main__":
    

    import pytest
    pytest.main()
