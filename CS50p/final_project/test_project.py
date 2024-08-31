import pytest
from project import process_txtwidget_input, count_followers_n_following, analyze_followers, create_file
import os



@pytest.fixture
def sample_followers_n_following():
    followers = {"usr1", "usr2", "usr3"}
    following = {"usr2", "usr3", "usr4"}
    return followers, following



def test_analyze_followers(sample_followers_n_following):
    followers, following = sample_followers_n_following
    not_following_back, not_followed_back = analyze_followers(followers, following)

    assert not_following_back == ["usr4"]
    assert not_followed_back == ["usr1"]



def test_count_followers_n_following(tmp_path):
    followers_file = tmp_path / "followers.txt"
    following_file = tmp_path / "following.txt"

    followers_file.write_text("user1\nuser2\nuser3\n")
    following_file.write_text("user2\nuser3\nuser4\n")

    followers, following = count_followers_n_following(followers_file, following_file)

    assert followers == {"user1", "user2", "user3"}
    assert following == {"user2", "user3", "user4"}



def test_create_file(tmp_path):
    followers = {"user1", "user2", "user3"}
    followers_file = tmp_path / "followers.txt"

    create_file(followers, followers_file)

    assert followers_file.exists()

    with open(followers_file, "r") as file:
        lines = file.read().splitlines()
        assert sorted(lines) == sorted(followers)
