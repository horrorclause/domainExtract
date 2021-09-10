# domainExtract
Extract domains from a block of text using regex, and exports them to a clean file that is ready to be used as input.
the "file" variable is for the input list of text, and the "newList" variable is the output, a clean file of only extracted domains.

run with "python3 domainExtract.py"

The "file" variable is used to feed the text document with the domains that need to be extracted:

![image](https://user-images.githubusercontent.com/10188810/132138767-da4c4335-ecc4-43c4-a17f-c0ef5276089b.png)

The examples below show the input file with domains that have TLDs, SLDs, and TLDs with multiple nodes. These need to be extracted from the IP(0.0.0.0) and other text.

**ex:**

![image](https://user-images.githubusercontent.com/10188810/132138789-a9c0c746-3d9f-4225-b196-2f19f36ac38f.png)
![image](https://user-images.githubusercontent.com/10188810/132138868-096aecee-5294-48ef-8df7-b859d4c93a91.png)


The "newFileName" variable will prompt you to name your new output file once the script is run, and the "newList" variable is used to set the location the newly extracted domain list will be saved to. 

**ONLY MODIFY THE PATH:** 
![image](https://user-images.githubusercontent.com/10188810/132139056-da51063a-36d2-4af0-be79-ce1be8cf4c2f.png)


![image](https://user-images.githubusercontent.com/10188810/132138993-5e2a49c4-b0a1-4a06-b82f-45403de70ba3.png)



Here is an example of the new list name prompt when the script is run:
![image](https://user-images.githubusercontent.com/10188810/132139164-854d6d66-b3cc-4712-a3cd-84490ac4ee5e.png)

Here is the output, which show the extracted domains with the TLDs, extra nodes, and SLDs:

![image](https://user-images.githubusercontent.com/10188810/132139288-c28514aa-db4c-4a77-a934-e6112df6061c.png)
![image](https://user-images.githubusercontent.com/10188810/132139317-c857c39b-ff16-4fbc-9275-cbf5a127843d.png)

