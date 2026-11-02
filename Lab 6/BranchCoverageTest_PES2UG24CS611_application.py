import pytest
from pet_boarding import boarding_fee, admission_ok, checkout_status


# Boarding fee tests
def test_unknown_pet_type():
    with pytest.raises(ValueError, match="unknown pet type"):
        boarding_fee("hamster", 5, False)


def test_negative_days():
    with pytest.raises(ValueError, match="invalid days"):
        boarding_fee("cat", -1, False)


def test_within_included_days():
    assert boarding_fee("dog", 1, False) == 0


def test_premium_dog_included_days():
    assert boarding_fee("dog", 3, True) == 0


def test_cat_extra_days():
    assert boarding_fee("cat", 5, False) == 40


def test_dog_extra_days():
    assert boarding_fee("dog", 4, False) == 60


def test_cat_more_than_ten_extra_days():
    assert boarding_fee("cat", 15, False) == 360


def test_dog_more_than_ten_extra_days():
    assert boarding_fee("dog", 20, False) == 810


# Admission tests
def test_senior_pet_with_enough_vaccinations():
    assert admission_ok(12, 3, True) is True


def test_senior_pet_with_insufficient_vaccinations():
    assert admission_ok(12, 2, True) is False


def test_pet_younger_than_one_year():
    assert admission_ok(0, 3, False) is False


def test_adult_pet_with_enough_vaccinations():
    assert admission_ok(4, 2, False) is True


def test_adult_pet_with_insufficient_vaccinations():
    assert admission_ok(4, 1, False) is False


# Checkout tests
def test_checkout_open():
    assert checkout_status(30, True, False) == "open"


def test_checkout_late():
    assert checkout_status(15, True, False) == "late"


def test_checkout_closed():
    assert checkout_status(14, True, False) == "closed"


def test_weekend_checkout_cutoff():
    assert checkout_status(35, False, True) == "open"
