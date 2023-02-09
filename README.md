# retiabellarius

Disclaimer: this script was written by ChatGPT. I have no knowledge of python.

Retiabellarius, a pun between rete (net/web) and tabellarius (archivist), is a script that, provided with a list of urls, downloads their first instance retrievable in the Wayback Machine.

This is particularly useful to quickly gather documentation provided throughout a given website, that might not be easily accessible anymore. 

To generate the list of urls to feed retiabellarius with, type the first bits of the website you are looking into https://web.archive.org/ but stop before any specific file is named.

Then click on URLs, filter them as PDF  or whatever it is you're looking for, and copy them. I copy them to excel, where I add the necessary format for python (urls must be inside quotation marks and separated by commas).

From Excel, copy them into the script and run it. Outcome files will appear in the same folder as the script.
