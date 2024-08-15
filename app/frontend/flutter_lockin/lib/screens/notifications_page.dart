import 'package:flutter/material.dart';
import 'home_page.dart';
import 'communities_page.dart';
import 'create_content.dart';
import 'personalization_page.dart';

class NotificationsPage extends StatefulWidget {
  @override
  NotificationsPageState createState() => NotificationsPageState();
}

class NotificationsPageState extends State<NotificationsPage> {
  int _selectedIndex = 3; // Start with Notifications selected

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
    } else if (index == 2) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => ContentCreationPage()),
      );
    } else if (index == 4) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(builder: (context) => PersonalizationPage()),
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
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: ListView(
          children: [
            Text(
              'Notifications',
              style: TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Colors.black,
              ),
            ),
            SizedBox(height: 20),
            _buildNotificationItem(
              imageUrl: 'https://via.placeholder.com/150', // Replace with actual image URL
              title: 'Sarah Connor',
              subtitle: 'Hey! Check out my new video on...',
              time: '2h ago',
            ),
            _buildNotificationItem(
              imageUrl: 'https://via.placeholder.com/150', // Replace with actual image URL
              title: 'John Smith',
              subtitle: 'Thanks for the feedback on my tutorial...',
              time: '5h ago',
            ),
            _buildNotificationItem(
              imageUrl: 'https://via.placeholder.com/150', // Replace with actual image URL
              title: 'Alice Brown liked your video',
              subtitle: '',
              time: '1h ago',
            ),
            _buildNotificationItem(
              imageUrl: 'https://via.placeholder.com/150', // Replace with actual image URL
              title: 'Michael Lee commented on your video:',
              subtitle: '"Great explanation!"',
              time: '3h ago',
            ),
            _buildNotificationItem(
              imageUrl: 'https://via.placeholder.com/150', // Replace with actual image URL
              title: 'Emma Watson shared your video',
              subtitle: '',
              time: '4h ago',
            ),
          ],
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

  Widget _buildNotificationItem({
    required String imageUrl,
    required String title,
    required String subtitle,
    required String time,
  }) {
    return Card(
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(15.0),
      ),
      child: ListTile(
        leading: CircleAvatar(
          backgroundImage: NetworkImage(imageUrl),
        ),
        title: Text(
          title,
          style: TextStyle(fontWeight: FontWeight.bold),
        ),
        subtitle: subtitle.isNotEmpty ? Text(subtitle) : null,
        trailing: Text(
          time,
          style: TextStyle(color: Colors.grey),
        ),
      ),
    );
  }
}
