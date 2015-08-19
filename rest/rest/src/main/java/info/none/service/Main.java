package info.none.service;

import org.glassfish.grizzly.http.server.HttpServer;

import com.sun.jersey.api.container.grizzly2.GrizzlyServerFactory;
import com.sun.jersey.api.core.PackagesResourceConfig;
import com.sun.jersey.api.core.ResourceConfig;

public class Main {
	public static void main(String... args) throws Exception {
		ResourceConfig rc = new PackagesResourceConfig("info.none.service.rest");
		HttpServer server = GrizzlyServerFactory.createHttpServer("http://localhost:8080", rc);
		server.start();
		for(;;) {
			Thread.sleep(1000);
		}
	}
}
