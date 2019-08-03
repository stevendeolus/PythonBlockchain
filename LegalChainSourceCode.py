
import hashlib as hasher
from random import randint
import random, string

import datetime
now = datetime.datetime.now()
print('' * 2)
print(r"""
      █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
      █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
      █░░║║║╠─║─║─║║║║║╠─░░█   
      █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
      █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
          TO Legal CHAIN

        ▇=-▇=-=▇-▇-=-▇=-=▇

""")

blockchain = [{'index': 0, 'data': '2019-03-15 01:48', 'host': 'computer',
               'current hash': 'fb045c275be6538217de9cacb5d4d46f7db0e79efa9dc759681aafd0cc0c8658','contentID': 'SDPS4TS7G48RXSctDI', 'category': 'song'}]

def verify_immutability():
    if len(blockchain) == 1:
        ran_index = 0 
    elif len(blockchain) >= 2:
        ran_index = randint(0, len(blockchain) - 1)
    else:
        print('there is nothing in the blockchain...gasp')
    blockchain[ran_index]['data'] = "you're being hacked"
    index = 0
    for index,block in enumerate(blockchain):
        print('Hi Mike', block)
        blockchain[index]['current hash']
        sha = hasher.sha256()
        sha.update(str(blockchain[index]['index']).encode('utf-8') + str(blockchain[index]['data']).encode('utf-8') + str(blockchain[index]['host']).encode('utf-8') + str(blockchain[index]['category']).encode('utf-8') + str(blockchain[index]['contentID']).encode('utf-8'))
        # print(sha.hexdigest())
        # I can uncomment the print code above this if I want the actual hash to be printed out
        index = 0
        chash = sha.hexdigest()
        if blockchain[index]['current hash'] != chash:
            blockchain.clear()
            print ('The Verify Immutability Program is running...')
            print('ERROR - ERROR - ERROR : BLOCKCHAIN HAS BEEN HACKED. EXITING BLOCKCHAIN IMMEDIATELY!!!!')
            print('The Blockchain has been deleted')

def assignID():
    ID = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return ID

def transfer():
  verifyContentID = input('Enter the content ID of the content you would like to transfer: ')
  index = 0
  type_of_content_three = True
  while type_of_content_three: 
    for index, block in enumerate(blockchain):
      if verifyContentID == blockchain[index]['contentID']:
        verifybc_content = blockchain[index]['category']
        contentIDMatch = True
        print('' * 2)
        print('Categories of where the content will be transferred')
        print('Y - Youtube')
        print('C - Computer')
        print('S - Spotify ')
        print('A - Apple Music')
        print('O - Other')
        print('' * 2) 
        print('' * 1)
        host = input('What platform do you want to transfer the asset to?')
        if host == 'Y' or host =='y':
          if verifybc_content == "Other":
            print('' * 1)
            print('Invalid. You are not allowed to transfer this content to this platform. Please choose another platform')
          else:
            host = 'Youtube'
            transferAsset = 'yes'
            bc_content = blockchain[index]['category']
            type_of_content_three = False
        elif host == 'c' or host =='C':
            host = 'Computer'
            transferAsset = 'yes'
            bc_content = blockchain[index]['category']
            type_of_content_three = False
        elif host == 's' or host =='S':
          if verifybc_content == "Image" or verifybc_content == "Video Content":
            print('' * 1)
            print('Invalid. You are not allowed to transfer this content to this platform. Please choose another platform')
          else:
            host = 'Spotify'
            transferAsset = 'yes'
            bc_content = blockchain[index]['category']
            type_of_content_three = False
        elif host == 'a' or host =='A':
          if verifybc_content == "Image" or verifybc_content == "Video Content":
            print('' * 1)
            print('Invalid. You are not allowed to transfer this content to this platform. Please choose another platform')
          else:
            host = 'Apple Music'
            transferAsset = 'yes'
            bc_content = blockchain[index]['category']
            type_of_content_three = False
        elif host == 'O' or host =='o':
            host = input('Please describe where this content will be stored ')
            transferAsset = 'yes'
            bc_content = blockchain[index]['category']
            type_of_content_three = False
        else:
            print('Invalid input')
        return(host,bc_content,verifyContentID,transferAsset)
      else:
        transferAsset = 'no'
        contentIDMatch = False

    if contentIDMatch == True:
      type_of_content_three = False
    else:
      print('' * 2)
      print('None of the assets tracked by this Blockchain has that content ID')
      transferAsset = 'no'
      bc_content = 'NAN'
      host = 'NAN'
      verifyContentID = 'NAN'
      type_of_content_three = False
    type_of_content_three = False
  return (host, bc_content,verifyContentID, transferAsset)

def add_value(host, bc_content, verifyContentID, data=now.strftime("%Y-%m-%d %H:%M")):
    index = 0
    if len(verifyContentID) > 0:
      contentID = verifyContentID
      print('' * 2)
    else:
      contentID = assignID()
    for block in blockchain:
        index += 1
        sha = hasher.sha256()
        sha.update(str(index).encode('utf-8') + str(data).encode('utf-8') + str(host).encode('utf-8') + str(bc_content).encode('utf-8')+ str(contentID).encode('utf-8')) 
        # print(sha.hexdigest())
        # I can uncomment the print code above this if I want the actual hash to be printed out
        chash = sha.hexdigest()

        if index == 1:
            phash = blockchain[0]['current hash']
        elif index > 1:
            phash = blockchain[index - 1]['current hash']

        transaction = {'index': index,'contentID': contentID,'data': data,'host': host,'category': bc_content,'current hash': chash,'previous hash': phash,}
        
        if index == 1:
            psha = hasher.sha256()
            psha.update(str(blockchain[0]['index']).encode('utf-8') + str(blockchain[0]['data']).encode('utf-8') + str(blockchain[0]['host']).encode('utf-8') + str(blockchain[0]['category']).encode('utf-8') + str(blockchain[0]['contentID']).encode('utf-8'))
            cpsha = psha.hexdigest()
        # Here I am rehashing the information in the previous dictionary in the blockchain to make sure nothing was changed. If nothing was changed I will add the transaction to the blockchain.
        elif index > 1:  # check that this is else if is correct
            psha = hasher.sha256()
            psha.update(str(blockchain[index - 1]['index']).encode('utf-8') + str(blockchain[index - 1]['data']).encode('utf-8') + str(blockchain[index - 1]['host']).encode('utf-8') + str(blockchain[index - 1]['category']).encode('utf-8') + str(blockchain[index - 1]['contentID']).encode('utf-8'))
            cpsha = psha.hexdigest()
        else:
            print('ERROR - ERROR - ERROR : BLOCKCHAIN WAS HACKED. GENISIS BLOCK IS MISSING. EXITING BLOCKCHAIN IMMEDIATELY!!!!')
            blockchain.clear()
            break

        #below - remember that phash is the previous hash
        if phash == cpsha:  
            # THE LAST THING I HAVE TO DO HERE IS TRY TO FIGURE OUT HOW TO GET THIS TO WORK WITH THE GENESIS BLOCK. The logic should say if the index is 1 add the transaction and if not it should go through the verification process.
            print ('Blockchain is error free')
            print (cpsha)
            print (phash)
            #I may have a hidden bug here because without the break it keeps looping. However, the other issue is the function is not grabbing the correct previous hash!
        else:
            blockchain.clear()
            print('ERROR - ERROR - ERROR : BLOCKCHAIN HAS BEEN HACKED. EXITING BLOCKCHAIN IMMEDIATELY!!!!')
            print ('the current previous hash is:')
            print (cpsha)
            print ('the previous hash is:')
            print (phash)
            #note on 3.26.19 - there is a bug that is making the else run. I need to figure out why this is happening. 

    if len(blockchain) == 0:
        blockchain.clear()
        waiting_for_input = False
    else:
        blockchain.append(transaction)
    print (blockchain)
    print('-' * 50)
    print('-' * 50)
    # return sha.hexdigest()
    # I should write a forumla here to doublecheck the blockchain to make sure nothing was changed. This should probably be an if statement. If the blockchain was changed the program should automatically be exited.


def add_content_to_blockchain():
    print('' * 2)
    print('This blockchain can track the following categories of content:')
    print('v - Video Content')
    print('m - Music')
    print('s - Sound Recording')
    print('i - Image')
    print('o - Other')
    print('' * 2)
    type_of_content = True
    while type_of_content: 
        bc_content = input('What type of content would you like to register to be tracked wiith the blockchain? \nType the corresponding letter for the categories of content from the list above:')
        #bc means BlockChain
        if bc_content == 'v' or bc_content =='V':
            bc_content = 'Video Content'
            type_of_content = False
        elif bc_content == 'm' or bc_content =='M':
            bc_content = 'Music'
            type_of_content = False
        elif bc_content == 's' or bc_content =='S':
            bc_content = 'Sound Recording'
            type_of_content = False
        elif bc_content == 'i' or bc_content =='I':
            bc_content = 'Image'
            type_of_content = False
        elif bc_content == 'O' or bc_content =='o':
            bc_content = input('Please describe the content you will track on the blockchain ')
            type_of_content = False
        else:
            print('Invalid input')
    print('' * 2)
    print('Categories where the content is stored')
    print('Y - Youtube')
    print('C - Computer')
    print('S - Spotify ')
    print('A - Apple Music')
    print('O - Other')
    print('' * 2)
    type_of_content_two = True
    while type_of_content_two: 
        host = input('What platform is this content hosted on?')
        if host == 'Y' or host =='y':
            host = 'Youtube'
            type_of_content_two = False
        elif host == 'c' or host =='C':
            host = 'Computer'
            type_of_content_two = False
        elif host == 's' or host =='S':
            host = 'Spotify'
            type_of_content_two = False
        elif host == 'a' or host =='A':
            host = 'Apple Music'
            type_of_content_two = False
        elif host == 'O' or host =='o':
            host = input('Please describe the content you will track on the blockchain')
            type_of_content_two = False
        else:
            print('Invalid input')
    #all recipient need to be changed to host
    verifyContentID = ''
    return (bc_content, host, verifyContentID)
#video music sound recording image - these are the categories I will use

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input

waiting_for_input = True

while waiting_for_input:
    print('' * 2)
    print('Please type one of the following options below: ')
    print('a - Add content meta data to the blockchain')
    print('h - Check blockchain immutability')
    print('p - Print the entire blockchain')
    print('t - Transfer asset to another platform')
    print('q - Quit Program')
    print('' * 2)
    user_choice = get_user_choice()
    if user_choice == 'a' or user_choice == 'A' :
        blockChain_data = add_content_to_blockchain()
        # blockChain_data is storing a tuple
        bc_content, host, verifyContentID = blockChain_data
        # Here I am taking the tuple and assigning the values to variables. I just so happens I am using the same variables as the function above.
        add_value(host, bc_content, verifyContentID)
        #3.11.19 Steve use a print statement to figure out what is happening when the function is storing a tuple
    elif user_choice == 'q' or user_choice == 'Q':
        waiting_for_input = False
    elif user_choice == 't' or user_choice == 'T':
      if len(blockchain) <= 1:
        print('There is not enough content on the blockchain to enable a transfer of an asset. Please add content to the Blockchain')
        AuthorizedToTransfer = 'no'

      else:
        transferOnBlockchain = transfer()
        AuthorizedToTransfer = 'yes'

      if AuthorizedToTransfer == 'no':
        print('')
      else:
        host, bc_content, verifyContentID,transferAsset = transferOnBlockchain
        if transferAsset == 'yes':
          add_value(host, bc_content, verifyContentID)
    elif user_choice == 'p' or user_choice == 'P' :
        for x in blockchain:
            print('')
            print(x)
            print('-' * 50)
            print('')
    elif user_choice == 'h' or user_choice == 'H':
        if len(blockchain) >= 1:
            verify_immutability()
        elif len(blockchain) < 1:
          print('')
          print('There is something wrong here. There is nothing in the blockchain')
          print('')
          print('')
          print('Exiting Legal Chain....')
          waiting_for_input = False
print(blockchain)
print('')
print('')
print(r"""
☆              ☆
 (\.   \      ,/)
  \(   |\     )/
  //\  |_\   /\\
 (/ /\_#oo#_/\ \)
  \/\  ####  /\/
     | `##' |
   Coded and made with love 
   by ASCII ~ /aeski/
              """)
