- The code starts by checking if the TLS library is enabled.
- If it is, then a function called tlsInitHandshake() will be called.
- This function takes in an argument of type TlsContext which is a pointer to the TLS context object that was created when the application started up.
- The first thing this function does is call another function named analyze_record().

- analyze_record() checks for any errors and returns an error code back to tlsInitHandshake().
- Then, tlsInitHandshake() calls dtlsRecordWrite(), which writes out data from memory into a DTLS record buffer.
- It also calls dtlsRecordRead(), which reads data from the DTLS record buffer and sends it over to client or server side of the connection as appropriate (depending on whether you are using TCP or UDP).- The code is the beginning of a function that initializes the TLS handshake.

- The first line sets up a pointer to the TLS context and returns an error code.

- The next line is where the actual initialization begins.- The code starts by allocating a send and receive buffer.
- If the buffers are not allocated, then they will be allocated with tlsAllocMem().
- The code also clears the buffers before using them.

- Next, it checks to see if this is a server connection or not.
- If so, then it allocates an extra buffer for sending data called entity (which is defined in TLS_CONNECTION_END_SERVER).
- This extra buffer can be used when there is no space left in the other two buffers because of how many bytes have been sent already.- The code attempts to allocate memory for the send and receive buffers.

- If the server mode is true, then the code allocates a buffer for sending data.
- If not, it allocates a buffer for receiving data.- The code starts by setting the context to TLS_STATE_CLIENT_HELLO.
- This is a state that indicates that the client has initiated a TLS handshake and is waiting for the server's response.
- The client then sends a ClientHello message to the server, which will analyze it and respond with its own ServerHello message.

- The code starts by analyzing whether or not early data was rejected.
- If so, then this means that there was an error in processing of some data before it could be sent over TLS (e.g., if you tried to send too much data).
- In this case, we set earlyDataRejected = TRUE; otherwise, we set earlyDataRejected = FALSE; meaning that everything went smoothly and no errors occurred during processing of any data before sending it over TLS.- The code is a server implementation of the TLS handshake.

- The code starts by declaring the context object as an instance of tls_context.

- 	//A server implementation may choose to reject the early data 		context->earlyDataRejected = TRUE;

- Next, it declares that when the client initiates a TLS handshake, it will be rejected with an error code of NO_ERROR.
- #ifdef __cplusplus

- 	extern "C" { 		} // end extern "C"

- #endif- The code starts by declaring a pointer to the TLS context.

- The code then declares a variable called error and initializes it with an error_t type.
- This is done because this function will return an error code, which is defined as an integer value in C++.
- The next line of code sets the value of the context pointer to NULL so that any subsequent calls to tlsPerformHandshake() will fail if they are made after this point in time.

- Next, the function checks whether DTLS support has been enabled or not using a conditional statement: if(context->transportProtocol == TLS_TRANSPORT_PROTOCOL_DATAGRAM) .
- If DTLS support has been enabled, then it means that we are dealing with a connection end-point where both sides have agreed on using DTLS for their communication channel; otherwise, we would be dealing with either client or server mode (which do not use DTLS).
- In order to determine what kind of handshake message needs to be sent out from our side, we need firstly know what type of handshake message was received from the other side.
- To do this, we call tlsGetMessageType() , which returns us one of three- The code is meant to be used in the context of a TLS handshake.

- The code starts by checking if the entity of the TLS context is set to "TLS_CONNECTION_END_CLIENT" or "TLS_CONNECTION_END_SERVER".
- If it is set to "TLS_CONNECTION_END_CLIENT", then an error will be returned and no further action will be taken.
- If it is set to "TLS_CONNECTION_END_SERVER", then an error will be returned and no further action will be taken.

- If it was not determined that the entity of the TLS context was either "TLS_CONNECTION _ END _ CLIENT- The code starts by pointing to the handshake message header.
- The data pointer is then set to point to the first byte of the handshake message, which is a DtlsHandshake type.
- Next, length bytes are copied from data into memory at location message->data and then that address is changed to point to location message->length.
- Finally, msgType and msgSeq are set for this new handshake message type and its sequence number in context's txMsgSeq variable is stored as htons(context->txMsgSeq).

- The fragment offset (0) and fragment length (length) variables are also set for this new handshake message type.- The code is the first step in a handshake message.
- It copies the data from the incoming packet into a DtlsHandshake object, which is then used to construct a handshake message header.

- The next step in this code is to make room for the handshake message header by moving it over and overwriting any existing data.
- The final step of this code is to send out the handshake message type, number of bytes in the message, sequence number, fragment offset, and fragment length.- The code starts by checking if the message is a handshake.
- If it is, then the code increments the txMsgSeq variable and makes room for the handshake header.
- The data pointer points to where in memory we want to store our handshake message header.
- Then, we make room for that header by moving everything up one byte so that it starts at offset 0x00 (the first byte of memory).

- Next, we check if this is a TLS protocol message or not.
- If it's not, then there are no more steps to take because this isn't a TLS protocol message type (i.e., DTLS_HANDSHAKE).
- However, if it's a TLS protocol message type (i.e., DTLS_HEARTBEAT), then there are additional steps to take: We need to make space for an empty TlsHandshake structure and point our data pointer at its beginning so that when we write into its fields later on they will be written into their proper locations in memory instead of overwriting other things with them like they would otherwise do without these extra steps taken beforehand .

- After making space for an empty TlsHandshake structure and pointing our data pointer at its beginning, we can now start- The code is the first code that is executed in case of a handshake message.

- The code is the last code that is executed in case of a handshake message.

- The code increments the sequence number by one when a new message is generated.

- This means that if there are two messages, then the sequence number will be 3 and 4 respectively.- The code starts by checking to see if the type of message is TLS_TYPE_HELLO_REQUEST.
- If it is, then the code will update the transcript hash and send a handshake message.

- If not, then the code checks to see if DTLS support has been enabled in this context.
- If so, then it sends a handshake message with DTLS protocol.- The code is a part of the TLS_TRANSPORT_PROTOCOL_DATAGRAM protocol.

- The code above checks if the transport protocol is DTLS, and if so, it sends the handshake message.- The code starts by checking if the transport protocol is DTLS.
- If it is, then the code checks to see if DTLS support has been enabled.
- If so, then a call to tlsReadProtocolData() will be made with the data length set to 0 and type set to TLS_TYPE_HANDSHAKE.

- If not, then a call will be made with the data length set to 0 and type set to TLS_TYPE_PROTOCOLDATA.
- This means that this function will read in any handshake message from the peer without knowing what kind of handshake message it might be (i.e., whether it's an application layer or transport layer).- The code attempts to receive a handshake message from the peer.

- The code will first check if the transport protocol is DTLS, and then proceed with the following steps:

- 1) Check if there is data in the buffer.
- If not, error = dtlsReadProtocolData(context, data, length);

- 2) Check if there are more bytes available in the buffer.
- If not, error = dtlsReadProtocolData(context, data + length - 1);

- 3) Send handshake message; 	4) Return status code.- The code starts by checking the status code of the dtlsReadProtocolData() function.
- If it returns an error, then the message is not a DTLS or TLS protocol and so we need to call tlsReadProtocolData().

- The next step in this function is to check if the content type of the received data matches TLS_TYPE_HANDSHAKE.
- If it does, then we parse out that handshake message and store its contents into memory.
- Then we advance our data pointer by length bytes and update our receive buffer's size accordingly.
- We also update our receive buffer's current position with length bytes worth of data from where they were previously stored in memory.

- If contentType doesn't match TLS_TYPE_HANDSHAKE, then we check for a ChangeCipherSpec message instead using contentType as a key value pair in order to determine what kind of message was received.- The code is a snippet of the code that we will be looking at in detail.

- The following line of code sets up a context for our TLS/DTLS communication:

- 	context = dtlsCreateContext(socket, &data, &length);

- This function creates a DTLS context on the socket and assigns it to the variable context.
- The data parameter is the buffer where we will store incoming messages from the remote peer.
- The length parameter is how many bytes are in this buffer.
- Finally, contentType tells us what type of message this is (e.g., TLS_TYPE_HANDSHAKE).
- If you want to see all of these values in one place, check out my Github repo for my project:- The code starts by checking the content type of the message.
- If it is TLS_TYPE_ALERT, then an alert message has been received and parsed.
- If not, then the code checks to see if a change cipher spec was sent in this message.

- If so, then the code parses out that information and sends it on to tls13ProcessEarlyData().
- Otherwise, if no change cipher spec was sent in this message, then the code checks for application data.
- In server mode (if enabled), any early data will be processed before sending anything else; otherwise, all other messages are processed first.- The code attempts to parse the incoming data and determine whether it's an alert message or application data.

- If the incoming data is an alert message, then the code will process that alert message and send back a response.
- If the incoming data is application data, then the code will process that application data and send back a response.- The code starts by checking to see if the transport protocol is DTLS.
- If it is, then a pointer to the handshake message type is retrieved and stored in msgType.
- The length of the handshake message is calculated using this value.

- If not, then a pointer to the TLS handshake message type is retrieved and stored in msgType.
- The length of the handshake message is calculated using this value.- The code is what is executed when the application receives a handshake message.

- The code above checks to see if the transport protocol of the received message is DTLS or TLS.
- If it's DTLS, then it will retrieve the DtlsHandshake type from the received message and point to its location in memory.
- The length of this type will be calculated by subtracting sizeof(DtlsHandshake) from length - sizeof(DtlsHandshake).

- If it's TLS, then it will retrieve the TlsHandshake type from the received message and point to its location in memory.
- The length of this type will be calculated by subtracting sizeof(TlsHandshake) from length - sizeof(TlsHandshake- The code starts by checking if the message type is TLS_TYPE_KEY_UPDATE.
- If it is, then a key update has been received and the code will process it.
- The next section of code checks to see if this is a client connection end or server connection end.
- If it's a client connection end, then the code parses out the handshake message from the server and sends back an error in case there was something wrong with that part of the handshake.

- If this is not a client connection end, then we check to see if this is a server connection end or not.
- If so, then we parse out what's inside of that message and send back an error in case there was something wrong with that part of the handshake as well.- The code does the following:

- If the current message type is not a key update, it will reset the count of consecutive key updates.

- If the current message type is a client handshake, it will parse server's handshake message.
