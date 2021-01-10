import instaloader
mod = instaloader.Instaloader()
a=input("ENTER USER NAME   :  ")
mod.download_profile(a,profile_pic_only = True)
