import java.io.*;
import java.net.*;
import java.util.Arrays;

class TCPServer {
	
	  public static String sortString(String inputString)
	    {
	        char tempArray[] = inputString.toCharArray();
	          
	        Arrays.sort(tempArray);
	         
	        return new String(tempArray);
	    }
	      
  public static void main(String argv[]) throws Exception
    {
	  
      String clientSentence;
      String sortedSentence;

      ServerSocket welcomeSocket = new ServerSocket(6789);
     
      while(true) {

                   Socket connectionSocket = welcomeSocket.accept();
                   System.out.println("[SERVIDOR]: PAI TA ON \n");
           BufferedReader inFromClient =
             new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));
           
           DataOutputStream  outToClient =
             new DataOutputStream(connectionSocket.getOutputStream());
           clientSentence = inFromClient.readLine();    
           System.out.println("[SERVIDOR]: " + clientSentence);
           sortedSentence = sortString(clientSentence);   
           outToClient.writeBytes("SEGURA TUA FRASE ORDENADA, PAI: "+sortedSentence+'\n');
           
           
       }  
    } 
}
