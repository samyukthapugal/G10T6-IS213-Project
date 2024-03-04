package microservice.activitylog;

import com.google.auth.oauth2.GoogleCredentials;
import com.google.cloud.firestore.Firestore;
import com.google.firebase.FirebaseApp;
import com.google.firebase.FirebaseOptions;
import com.google.firebase.cloud.FirestoreClient;
import org.springframework.stereotype.Service;
import org.springframework.util.ResourceUtils;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

@Service
public class FirebaseConfig {

	public static void initializeWithDefaultCredentials() throws IOException {
		// [START initialize_sdk_with_application_default]
		File file = ResourceUtils.getFile("classpath:esd-activity-log-firebase-adminsdk-iz6ue-81a21dc864.json");
		FileInputStream serviceAccount = new FileInputStream(file);

		FirebaseOptions options = FirebaseOptions.builder()
				.setCredentials(GoogleCredentials.fromStream(serviceAccount))
				.setDatabaseUrl("https://esd-activity-log-default-rtdb.asia-southeast1.firebasedatabase.app")
				.build();

		FirebaseApp.initializeApp(options);
		Firestore db = FirestoreClient.getFirestore();
		// [END initialize_sdk_with_application_default]
	}

}