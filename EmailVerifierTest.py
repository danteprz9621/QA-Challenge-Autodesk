from assertpy import assert_that
from EmailVerifier import EmailVerifier

# Example emails with expected results
email1 = "winston.ctl@codechallenge.com"  # Expected: true
email2 = "jonathanisgreat"  # Expected: false
email3 = None  # Expected: false
email4 = ""  # Expected: false
email5 = "bella-@codechallenge.com"  # Expected: true
email6 = "winston#2024@codechallenge.com"  # Expected: false
email7 = "winston2024@coooddddeeeee.com"  # Expected: false
email8 = "-winston-@codechallenge.com"  # Expected: false


class TestEmail:
    verifier = EmailVerifier()

    def test_email1(self):
        assert_that(self.verifier.is_valid_email(email1)).is_true()

    def test_email2(self):
        assert_that(self.verifier.is_valid_email(email2)).is_false()

    def test_email3(self):
        assert_that(self.verifier.is_valid_email(email3)).is_false()

    def test_email4(self):
        assert_that(self.verifier.is_valid_email(email4)).is_false()

    def test_email5(self):
        assert_that(self.verifier.is_valid_email(email5)).is_true()

    def test_email6(self):
        assert_that(self.verifier.is_valid_email(email6)).is_false()

    def test_email7(self):
        assert_that(self.verifier.is_valid_email(email7)).is_false()

    def test_email8(self):
        assert_that(self.verifier.is_valid_email(email8)).is_false()
