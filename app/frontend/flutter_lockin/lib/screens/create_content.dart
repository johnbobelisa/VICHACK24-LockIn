import 'dart:io';
import 'package:firebase_storage/firebase_storage.dart';
import 'package:file_picker/file_picker.dart';
import 'package:flutter/material.dart';
import 'home_page.dart';
import 'communities_page.dart';
import 'personalization_page.dart';
import 'notifications_page.dart';

class ContentCreationPage extends StatefulWidget {
  @override
  ContentCreationPageState createState() => ContentCreationPageState();
}

class ContentCreationPageState extends State<ContentCreationPage> {
  int _selectedIndex = 2; // Start with Content Creation selected

  Future<void> _uploadVideo(String folderName) async {
    // Let the user pick a file
    FilePickerResult? result = await FilePicker.platform.pickFiles(
      type: FileType.video,
    );

    if (result != null) {
      // Get the file path
      String filePath = result.files.single.path!;

      // Create a storage reference
      FirebaseStorage storage = FirebaseStorage.instance;
      Reference ref = storage.ref().child('$folderName/${DateTime.now().millisecondsSinceEpoch}.mp4');

      // Upload the file to Firebase
      UploadTask uploadTask = ref.putFile(File(filePath));

      // Monitor the upload progress
      uploadTask.snapshotEvents.listen((TaskSnapshot snapshot) {
        print('Progress: ${(snapshot.bytesTransferred / snapshot.totalBytes) * 100} %');
      });

      // Wait for the upload to complete
      TaskSnapshot taskSnapshot = await uploadTask;

      // Get the download URL of the uploaded video
      String downloadURL = await taskSnapshot.ref.getDownloadURL();
      print('Video URL: $downloadURL');
    }
  }

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });

    if (index == 0) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => HomePage()),
      );
    } else if (index == 1) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => CommunitiesPage()),
      );
    } else if (index == 4) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => PersonalizationPage()),
      );
    } else if (index == 3) {
      Navigator.pushReplacement(
          context,
          MaterialPageRoute(builder: (context) => NotificationsPage())
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xFF1e3a8a),
        title: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.lock,
              color: Colors.white,
            ),
            SizedBox(width: 8),
            Text(
              'LockIn',
              style: TextStyle(
                fontFamily: 'Roboto',
                color: Colors.white,
                fontWeight: FontWeight.bold,
              ),
            ),
          ],
        ),
        centerTitle: true,
        actions: [
          IconButton(
            icon: Icon(Icons.search),
            color: Colors.white,
            onPressed: () {
              showSearch(
                context: context,
                delegate: CustomSearchDelegate(),
              );
            },
          ),
        ],
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Text(
                'Generate AI Content from lectures!',
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF1e3a8a),
                ),
              ),
              SizedBox(height: 20),
              Card(
                elevation: 2,
                shape: RoundedRectangleBorder(
                  borderRadius: BorderRadius.circular(15.0),
                ),
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start, // Align text to the left
                    children: [
                      Text(
                        'Lecture Videos',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Color(0xFF1e3a8a),

                        ),
                      ),
                      SizedBox(height: 10),
                      ElevatedButton(
                        onPressed: () => _uploadVideo('videos/raw'), // Handle Lecture Video Upload
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Color(0xFF1e3a8a),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10.0),
                          ),
                          padding: EdgeInsets.symmetric(vertical: 15),
                          minimumSize: Size(double.infinity, 0), // Full width button
                        ),
                        child: Text(
                          'Upload Your Lecture Here!',
                          style: TextStyle(color: Colors.white),
                        ),
                      ),
                      SizedBox(height: 20),
                      Center(
                        child: Text(
                          'or',
                          style: TextStyle(fontSize: 16, color: Colors.black54),
                        ),
                      ),
                      SizedBox(height: 10),
                      Text(
                        'Lecture Slides',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.bold,
                          color: Color(0xFF1e3a8a),
                        ),
                      ),
                      SizedBox(height: 10),
                      ElevatedButton(
                        onPressed: () {
                          // Handle Lecture Slides Upload
                        },
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Color(0xFF1e3a8a),
                          shape: RoundedRectangleBorder(
                            borderRadius: BorderRadius.circular(10.0),
                          ),
                          padding: EdgeInsets.symmetric(vertical: 15),
                          minimumSize: Size(double.infinity, 0), // Full width button
                        ),
                        child: Text(
                          'Upload your lecture slides here! (pptx or .pdf)',
                          style: TextStyle(color: Colors.white),
                        ),
                      ),
                    ],
                  ),
                ),
              ),
              SizedBox(height: 100),
              Text(
                'Upload Your Own Video',
                style: TextStyle(
                  fontSize: 20,
                  fontWeight: FontWeight.bold,
                  color: Color(0xFF1e3a8a),
                ),
              ),
              SizedBox(height: 60),
              ElevatedButton(
                onPressed: () => _uploadVideo('videos/final'), // Handle Upload Video
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(0xFF1e3a8a),
                  shape: RoundedRectangleBorder(
                    borderRadius: BorderRadius.circular(10.0),
                  ),
                  padding: EdgeInsets.symmetric(vertical: 15, horizontal: 50),
                  minimumSize: Size(double.infinity, 0), // Full width button
                ),
                child: Text(
                  'Upload Video',
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ],
          ),
        ),
      ),
      bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.home),
            label: '',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.group),
            label: '',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.add),
            label: '',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.notifications),
            label: '',
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            label: '',
          ),
        ],
        currentIndex: _selectedIndex,
        selectedItemColor: Colors.white,
        unselectedItemColor: Colors.white70,
        backgroundColor: Color(0xFF1e3a8a),
        onTap: _onItemTapped,
        type: BottomNavigationBarType.fixed,
      ),
    );
  }
}

// Custom search delegate for the search functionality
class CustomSearchDelegate extends SearchDelegate {
  @override
  List<Widget> buildActions(BuildContext context) {
    return [
      IconButton(
        icon: Icon(Icons.clear),
        onPressed: () {
          query = '';
        },
      ),
    ];
  }

  @override
  Widget buildLeading(BuildContext context) {
    return IconButton(
      icon: Icon(Icons.arrow_back, color: Colors.white),
      onPressed: () {
        close(context, null);
      },
    );
  }

  @override
  Widget buildResults(BuildContext context) {
    return Center(
      child: Text("Search result for '$query'"),
    );
  }

  @override
  Widget buildSuggestions(BuildContext context) {
    return Center(
      child: Text("Suggestions for '$query'"),
    );
  }
}
