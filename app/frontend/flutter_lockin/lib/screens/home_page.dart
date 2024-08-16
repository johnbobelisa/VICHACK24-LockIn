import 'package:flutter/material.dart';
import 'personalization_page.dart'; // Import the PersonalizationPage
import 'communities_page.dart';
import 'create_content.dart';
import 'notifications_page.dart';
import 'package:video_player/video_player.dart';

class HomePage extends StatefulWidget {
  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  int _selectedIndex = 0;
  late VideoPlayerController _controller;
  bool _isInitialized = false;

  @override
  void initState() {
    super.initState();
    _initializeVideoPlayer();
  }

  Future<void> _initializeVideoPlayer() async {
    try {
      String videoUrl = await _fetchVideoUrlFromFirebase();

      _controller = VideoPlayerController.networkUrl(
        Uri.parse(videoUrl),
        videoPlayerOptions: VideoPlayerOptions(mixWithOthers: true),
      );

      await _controller.initialize().then((_) {
        setState(() {
          _isInitialized = true;
        });
        _controller.setLooping(true);
        _controller.play();
      });

    } catch (e) {
      setState(() {
        _isInitialized = false;
      });
    }
  }


  Future<String> _fetchVideoUrlFromFirebase() async {
    // Placeholder URL for now. Ensure this URL is valid and points to a video file.
    return 'https://flutter.github.io/assets-for-api-docs/assets/videos/bee.mp4';
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  static const List<Widget> _widgetOptions = <Widget>[
    // Your actual pages or widgets go here. I'm using placeholders for now.
    Text('Home Page', style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
    Text('Communities', style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
    Text('Add Content', style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
    Text('Notifications', style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
    Text('Profile', style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold)),
  ];

  void _onItemTapped(int index) {
    setState(() {
      _selectedIndex = index;
    });

    if (index == 4) {
      // Navigate to the PersonalizationPage when "personal icon" is selected
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => PersonalizationPage()),
      );
    } else if (index == 1) {
      Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => CommunitiesPage())
      );
    } else if (index == 2) {
      Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => ContentCreationPage())
      );
    } else if (index == 3) {
      Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => NotificationsPage())
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Color(0xFF1e3a8a), // Set AppBar color using color code
        title: Row(
          mainAxisSize: MainAxisSize.min,
          children: [
            Icon(
              Icons.lock,
              color: Colors.white, // Change icon color to white
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
            color: Colors.white, // Set the color of the search icon to white
            onPressed: () {
              // Define what happens when the search icon is pressed
              showSearch(
                context: context,
                delegate: CustomSearchDelegate(),
              );
            },
          ),
        ],
      ),
      body: Stack(
        children: [
          _isInitialized && _controller.value.isInitialized
              ? Positioned.fill(
            child: AspectRatio(
              aspectRatio: _controller.value.aspectRatio,
              child: VideoPlayer(_controller),
            ),
          )
              : Center(
            child: CircularProgressIndicator(),
          ),
          Positioned(
            bottom: 20,
            left: 20,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Storytime Adventures',
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 24,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  'Explore the exciting world of chemistry with hands-on experiments. #smart #educational',
                  style: TextStyle(
                    color: Colors.white70,
                    fontSize: 16,
                  ),
                ),
              ],
            ),
          ),
        ],
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
        backgroundColor: Color(0xFF1e3a8a), // Ensure background color is blue
        onTap: _onItemTapped,
        type: BottomNavigationBarType.fixed, // Ensures all items are visible and clickable
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
      icon: Icon(Icons.arrow_back),
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
