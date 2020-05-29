package edu.utn.ads.unknown_word_service;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

import com.rabbitmq.client.Channel;
import com.rabbitmq.client.Connection;
import com.rabbitmq.client.ConnectionFactory;
import com.rabbitmq.client.DeliverCallback;
import com.rabbitmq.client.GetResponse;

@RestController
public class PullWordsService {
    private final static String QUEUE_NAME = "unknown";

    @RequestMapping("/pull/")
	public String index() throws Exception {
        String message = null;
        ConnectionFactory factory = new ConnectionFactory();
        factory.setHost("172.17.0.5");
        Connection connection = factory.newConnection();
        Channel channel = connection.createChannel();

        channel.queueDeclare(QUEUE_NAME, false, false, false, null);
        System.out.println("Expecting messages");
        
        GetResponse response = channel.basicGet(QUEUE_NAME, true);
        if (response != null) {
            message = new String(response.getBody(), "UTF-8");
            System.out.println(" [x] Received '" + message + "'");
        }
        
        channel.close();
        connection.close();
        return message;
	}
}