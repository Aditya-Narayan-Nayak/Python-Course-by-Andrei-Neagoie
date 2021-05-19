is_magician = True
is_expert = False

# check  if magician and expert : "you are a master magician
if is_expert and is_magician:
    print("you are a master magician")

# check id magician but not expert :"at least you are getting there"
elif is_magician and not is_expert:
    print("at least you are getting there")

# if you are not a magician :"you need magic powers "
elif not is_magician:
    print("you need a magic power")

