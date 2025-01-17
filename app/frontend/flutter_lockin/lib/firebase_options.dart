// File generated by FlutterFire CLI.
// ignore_for_file: type=lint
import 'package:firebase_core/firebase_core.dart' show FirebaseOptions;
import 'package:flutter/foundation.dart'
    show defaultTargetPlatform, kIsWeb, TargetPlatform;

/// Default [FirebaseOptions] for use with your Firebase apps.
///
/// Example:
/// ```dart
/// import 'firebase_options.dart';
/// // ...
/// await Firebase.initializeApp(
///   options: DefaultFirebaseOptions.currentPlatform,
/// );
/// ```
class DefaultFirebaseOptions {
  static FirebaseOptions get currentPlatform {
    if (kIsWeb) {
      return web;
    }
    switch (defaultTargetPlatform) {
      case TargetPlatform.android:
        return android;
      case TargetPlatform.iOS:
        return ios;
      case TargetPlatform.macOS:
        return macos;
      case TargetPlatform.windows:
        return windows;
      case TargetPlatform.linux:
        throw UnsupportedError(
          'DefaultFirebaseOptions have not been configured for linux - '
          'you can reconfigure this by running the FlutterFire CLI again.',
        );
      default:
        throw UnsupportedError(
          'DefaultFirebaseOptions are not supported for this platform.',
        );
    }
  }

  static const FirebaseOptions web = FirebaseOptions(
    apiKey: 'AIzaSyBA4mcH77Byk9mPxw0ZuVoCm-hiLnOfwSw',
    appId: '1:672587067478:web:a1261e79f6a4ddf6888bf7',
    messagingSenderId: '672587067478',
    projectId: 'lockin-66341',
    authDomain: 'lockin-66341.firebaseapp.com',
    storageBucket: 'lockin-66341.appspot.com',
    measurementId: 'G-FS4TTL4WBY',
  );

  static const FirebaseOptions android = FirebaseOptions(
    apiKey: 'AIzaSyAjACQgPXr2odsWyTlOOb6aS7FQYwy_pO0',
    appId: '1:672587067478:android:855e3ec1bed83163888bf7',
    messagingSenderId: '672587067478',
    projectId: 'lockin-66341',
    storageBucket: 'lockin-66341.appspot.com',
  );

  static const FirebaseOptions ios = FirebaseOptions(
    apiKey: 'AIzaSyCQd_ccfvCyKdGdESgOH4oiOr8AAPzQo6s',
    appId: '1:672587067478:ios:c14c6595feda2cf4888bf7',
    messagingSenderId: '672587067478',
    projectId: 'lockin-66341',
    storageBucket: 'lockin-66341.appspot.com',
    iosBundleId: 'com.example.flutterLockin',
  );

  static const FirebaseOptions macos = FirebaseOptions(
    apiKey: 'AIzaSyCQd_ccfvCyKdGdESgOH4oiOr8AAPzQo6s',
    appId: '1:672587067478:ios:c14c6595feda2cf4888bf7',
    messagingSenderId: '672587067478',
    projectId: 'lockin-66341',
    storageBucket: 'lockin-66341.appspot.com',
    iosBundleId: 'com.example.flutterLockin',
  );

  static const FirebaseOptions windows = FirebaseOptions(
    apiKey: 'AIzaSyBA4mcH77Byk9mPxw0ZuVoCm-hiLnOfwSw',
    appId: '1:672587067478:web:8d9d173dc879347c888bf7',
    messagingSenderId: '672587067478',
    projectId: 'lockin-66341',
    authDomain: 'lockin-66341.firebaseapp.com',
    storageBucket: 'lockin-66341.appspot.com',
    measurementId: 'G-VHXNYLKT8N',
  );

}