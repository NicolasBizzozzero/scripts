""" Check who is not following you back on Github.

Source :
* https://github.com/six519/GitHub-Unfollower

Requirements :
* PyGithub >= 1.43.5
"""

from getpass import getpass

import github


def main(github_username, github_password, unfollow=False):
    user = login(github_username, github_password)
    followers = retrieve_followers_id(user)

    for following in user.get_following():
        if following.id not in followers:
            name = following.login if following.name is None else "%s (%s)" % \
                (following.login, following.name)
            print("Github user with ID: %s and Name: %s is not following you" %
                  (following.id, name))
            if unfollow:
                unfollow_that_bitch(user, bitch_to_unfollow=following)


def login(github_username, github_password):
    user = github.Github(github_username, github_password).get_user()

    try:
        user.name
        return user
    except github.GithubException:
        print("The script can't connect to Github with the given credentials")
        exit(1)


def retrieve_followers_id(user):
    following_count = 0
    followers_count = 0

    user_name = user.name
    user_id = user.id
    followers_count = user.followers
    following_count = user.following

    print("Your Github ID is: %s\nYour Github Name is: %s" %
          (user_id, user_name))
    print("You got %s followers and you are following %s Github users" %
          (followers_count, following_count))
    print("\n", end="")

    return [follower.id for follower in user.get_followers()]


def unfollow_that_bitch(user, bitch_to_unfollow):
    user.remove_from_following(bitch_to_unfollow)


if __name__ == "__main__":
    github_username = input("Please enter your Github username: ").strip()
    github_password = getpass("Please enter your Github password: ").strip()
    main(github_username, github_password)
