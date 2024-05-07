import java.rmi.registry.LocateRegistry;

import java.rmi.registry.Registry;

public class Client {

public static void main(String[] args) {

try {

Registry registry = LocateRegistry.getRegistry("localhost", 5555);

Adder stub= ( Adder) registry.lookup("Adder");

int result =stub.add(5, 3); System.out.println("Result: " + result);

} catch (Exception e) {





System.err.println("Client exception: " + e.toString());

e.printStackTrace();


}
}
}