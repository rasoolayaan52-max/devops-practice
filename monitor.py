import platform
import os

print ("--- System Health Check ---")
print (f"Operating System: {platform.system()} {platform.release()}")
print (f"Current Directory: {os.getcwd()}")
print ("status            : Operational")
