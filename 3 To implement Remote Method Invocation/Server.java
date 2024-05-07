import java.rmi.registry.LocateRegistry;

import java.rmi.registry.Registry;


public class Server {

public static void main(String[] args) {

try {

AdderImpl obj = new AdderImpl();

Registry registry =LocateRegistry.createRegistry(5555); registry.bind("Adder", obj);

System.out.println("Server ready");

} catch (Exception e) {

System.err.println("Server exception:"+  e.toString());
e.printStackTrace();
}

}

}