import java.io.*;
import java.net.*;

public class Master {
    public static void main(String args[]) {
        try {
            Socket MyClient = new Socket("127.0.0.1", 8881);
            System.out.println("Connected as Master");
            DataOutputStream dout = new DataOutputStream(MyClient.getOutputStream());
            BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));

            String send;
            do {
                System.out.print("Message ('stop' to end): ");
                send = reader.readLine();
                dout.writeUTF(send);
                dout.flush();
            } while (!send.equals("stop"));

            dout.close();
            MyClient.close();
        } catch (IOException e) {
            System.err.println("Error in Master: " + e.getMessage());
        }
    }
}

