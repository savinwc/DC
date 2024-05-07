import java.io.*;
import java.net.*;

public class Slave {
    public static void main(String args[]) {
        try {
            Socket MyClient = new Socket("127.0.0.1", 8881);
            System.out.println("Connected as Slave");
            DataInputStream din = new DataInputStream(MyClient.getInputStream());

            String received;
            do {
                received = din.readUTF();
                System.out.println("Master says: " + received);
            } while (!received.equals("stop"));

            din.close();
            MyClient.close();
        } catch (IOException e) {
            System.err.println("Error in Slave: " + e.getMessage());
        }
    }
}
