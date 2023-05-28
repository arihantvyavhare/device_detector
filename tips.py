
# %%
# Tips:
## downloading images using duckduckgo and fastbook
#* 
#* test

# %%
from fastbook import *

query = "joker"

urls = search_images_ddg(query, max_images = 5 )

len(urls)

# for url in urls : print(url)
# %%
for i,url in enumerate(urls):
    download_url(url,f"data/{query}/{query}_{i+1}.jpg")
# %%
import shutil 

shutil.rmtree(f"data/{query}")




