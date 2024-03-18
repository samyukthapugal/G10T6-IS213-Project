package microservice.activitylog;

import com.fasterxml.jackson.databind.JsonNode;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.postmarkapp.postmark.Postmark;
import com.postmarkapp.postmark.client.ApiClient;
import com.postmarkapp.postmark.client.data.model.message.Message;
import com.postmarkapp.postmark.client.data.model.message.MessageResponse;

import org.springframework.amqp.rabbit.annotation.RabbitListener;
import org.springframework.stereotype.Service;

import java.io.IOException;


@Service
public class Receiver {

	ApiClient client = Postmark.getApiClient("8ec71d6b-4d86-437a-ad24-c7f332cb49a5");

	@RabbitListener(queues = {"Activity_Log"})
	public void receiveMessage(String message) throws IOException {
		System.out.println("Received " + message);
		try {
			ObjectMapper mapper = new ObjectMapper();
			JsonNode rootNode = mapper.readTree(message);
			System.out.println(rootNode.path("email"));
        	Message msg = new Message("wsee.2023@scis.smu.edu.sg", rootNode.path("email").toString(), "Booking has been made", rootNode.path("message").path("data").toString());
        	MessageResponse response = client.deliverMessage(msg);
			System.out.println(response);
        } catch (Exception e) {
            // Handle email sending exception
            e.printStackTrace();
        }
	}
}
