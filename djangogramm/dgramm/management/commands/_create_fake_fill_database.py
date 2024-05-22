import random
from PIL import Image as pil
from io import BytesIO

from faker import Faker
from dgramm.models import User, Post, Image
from taggit.models import Tag

# width, height = (400, 700)

fake = Faker()


def create_image(width=333, height=777):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)

    image = pil.new("RGB", (width, height), color)

    buffer = BytesIO()
    image.save(buffer, format='PNG')
    buffer.seek(0)
    return buffer


def create_fake_tags():
    created_tags = []

    for tag_name in fake.words(20):
        tag, created = Tag.objects.get_or_create(name=tag_name)
        created_tags.append(tag)

    return created_tags


def create_user():
    username = fake.user_name()
    email = f'{username}@example.com'
    password = f'{username}password'
    first_name = fake.first_name()
    last_name = fake.last_name()
    bio = fake.sentence(nb_words=random.randint(10, 20))
    email_verify = 1

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        bio=bio,
        email_verify=email_verify,
    )
    user.avatar.save(f'avatar_{username}.png', create_image(), save=True)
    return user


def create_post(user):
    post = Post.objects.create(author=user)
    for _ in range(random.randint(1, 3)):
        image = Image.objects.create(post=post)
        image.image.save(f'filename_{user.username}.png', create_image(), save=True)
    return post


def main(users_count):
    users = [create_user() for _ in range(users_count)]
    tags = create_fake_tags()

    for user in users:
        for _ in range(random.randint(1, 21)):
            post = create_post(user)
            post.tags.add(*random.sample(tags, random.randint(1, 5)))

    posts = Post.objects.all()
    for post in posts:
        post.likes.add(*random.sample(users, random.randint(1, len(users))))
