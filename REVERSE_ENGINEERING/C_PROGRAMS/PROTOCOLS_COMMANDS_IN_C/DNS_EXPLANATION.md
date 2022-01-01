- The code starts by defining a struct called dns_query.
- This is the type of query that will be made, and it has two fields: one for the type of query (host->IP) and another for the name length.

- The next line defines a pointer to this struct called resolver.
- The resolver points to an instance of a DNS Resolver object which is defined in internal.h

- Next, we define some global variables like error code errno, user credentials cred, and slab size used by the kernel's memory allocator slabsize

- Then we define some functions that are needed later on in our program: lookup_name(), lookup_user(), getaddrinfo()

- Finally, we call out to these functions from main().- The code is the beginning of a DNS query.
- The first line declares that the function will be called with type as an argument and then it declares that the variable name will be used to store the name being looked up.

- The next line declares that namelen will be used to store the length of name.- The code is a function that takes in the following parameters:

- * @options: Request options (or NULL if no options)

- * @_result: Where to place the returned data (or NULL)

- * @_expiry: Where to store the result expiry time (or NULL)- The code is a function that returns the data in an array.

- The "domain_name" is the name of the domain, and the "query_type" is either "search", or "list".

- If there are no options passed to this function, then it will return an empty array.- The code starts by checking to see if the type is a straight hostname to IP address lookup.
- If it is, then the code calls dns_query_hostname() and passes in the name and namelen arguments.

- If not, then it checks for a query of type "A" which would be an A record lookup.
- If there is no query of type "A", then the code calls dns_query_ipv4().
- This function takes two arguments: name and options.
- The options argument can either be NULL or contain one option string that will be passed into getaddrinfo().
- The result argument points to where we want to store our answer from getaddrinfo(), while expiry stores the time when this answer expires (if any).

- The next step is getting a key with creds using creds->getkey() .
- Next, we save our current credentials so that they are available later on in case something goes wrong during execution of this function.
- Then we call upcallers using upcaller->upcall() .
- We pass in rkey as our key object pointer and saved_cred as our saved credentials pointer.
- Finally, after calling upcallers , we return 0 on success or -- The code is in a function called dns_query.

- The first parameter of the function is the type of query that needs to be performed.
- This can be either a hostname to IP address lookup or an A record lookup.
- The second parameter is the name being queried for, which should be in DNS format and not include any wildcards (e.g., "www.google.com" instead of "*.google.*").
- The third parameter specifies how many characters long the name is, and it should also not include any wildcards (e.g., "www."
- instead of "*.*").
- The fourth parameter specifies what options are needed for this particular query type, and it must match one of those options listed below:- The code starts by checking if the name is empty.
- If it is, then an error will be returned.
- Next, a string called options is created with all of the possible values for this query key.
- The code then creates a new variable called len that will hold the length of the option string in characters and assigns it to 0.

- Next, a pointer to type (which was declared earlier) is assigned to typelen and another pointer to desc (which was declared earlier) is assigned to desclen .
- Then, if type exists as a string value in options , then typelen will be set equal to strlen(type) and desclen will be set equal to 1 plus strlen(type)+1 .
- This means that when you have "foo:bar" as your option value, typelen would be 4 because there are four letters in "foo:bar".
- When you have "foo:" as your option value, though, only one letter would exist so typelen would just be 1 while desclen would still be 2 since there are two letters in "foo:"- The code starts by checking the input for a valid name and length.
- If the input is not valid, then it will return an error message.
- The code also checks to see if the user entered a type or not.
- If they did, then it will create a string with that length in order to build up the key description.

- The next step is to check if there was any input on what type of key this should be.
- If there was no input, then it will return an error message stating that this function does not exist yet.- The code starts by checking if the length of the string is less than 3 characters.
- If it is, then the program returns an error because there is not enough space to store a name in this format.
- Next, it allocates memory for a descriptor and copies the string into that buffer.
- The next line checks if type was passed as an argument and if so, it copies that string into the descriptor's buffer as well.
- Then at last, it appends a colon to indicate where we are in this list of names.

- The code starts by checking if namelen < 3 or namelen > 255 which means that they have already checked whether or not they can fit all of these names on one line without exceeding 255 characters (the maximum number of characters allowed).
- If either condition evaluates true then they will return -EINVAL which means "invalid operation".
- Next, desclen += namelen + 1; desc = kmalloc(desclen, GFP_KERNEL); cp = desc; *cp++ = ':'; memcpy(cp, type) ; cp += typelen; *cp++ = '\0'; options="";- The code will allocate a buffer of size desclen, which is the length of the string.
- The code will then copy in name, and append ':'.
- This is done to ensure that there are no null bytes at the end of the string.

- The next step in this snippet is to copy in type, and append ':'.
- This ensures that there are no null bytes at the beginning or end of the string.- The code starts by calling request_key() with the desc and options as arguments.
- The call is made to prevent malicious redirections from being preinstalled in the keyring.
- Next, saved_cred is overridden with a special credential that prevents add_key() from being called on it.
- Then rkey is created using request_key().
- If this succeeds, then revert_creds() restores saved_cred's credentials before freeing the descriptor and exiting if an error occurred.

- If rkey was successfully created, then down_read(&rkey->sem) will block until either a response or timeout occurs.- The code will first make an upcall to request_key() with the given options.

- The upcall is made using special credentials that prevent any malicious redirections from being installed by the add_key() function.

- The rkey variable is then set to point to the newly created key object.

- Finally, the saved creds are reverted back and a kfree() is called on desc, which will free up any memory used for storing this string.

