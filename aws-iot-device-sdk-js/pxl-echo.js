/*
 * Copyright 2010-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

//node.js deps

//npm deps

//app deps
const thingShadow = require('.').thingShadow;
const isUndefined = require('./common/lib/is-undefined');
const cmdLineProcess = require('./lib/cmdline');

var exec = require('child_process').exec;
var execSync = require('child_process').execSync;
var spawnSync = require('child_process').spawnSync;
var child;
//begin module

function processTest(args) {

   if (isUndefined(args.thingName)) {
      console.log('thing name must be specified with --thing-name');
      process.exit(1);
   }
   //
   // The thing module exports the thing class through which we
   // can register and unregister interest in thing shadows, perform
   // update/get/delete operations on them, and receive delta updates
   // when the cloud state differs from the device state.
   //
   const thingShadows = thingShadow({
      keyPath: args.privateKey,
      certPath: args.clientCert,
      caPath: args.caCert,
      clientId: args.clientId,
      region: args.region,
      baseReconnectTimeMs: args.baseReconnectTimeMs,
      keepalive: args.keepAlive,
      protocol: args.Protocol,
      port: args.Port,
      host: args.Host,
      debug: args.Debug
   });
   //
   // Register a thing name and listen for deltas.  Whatever we receive on delta
   // is echoed via thing shadow updates.
   //
   thingShadows.register(args.thingName, {
      persistentSubscribe: true
   });

   thingShadows
      .on('error', function(error) {
         console.log('error', error);
      });

   thingShadows
       .on('connect', function() {
          // Check for child state
          console.log("Kill check....");
          if (child){
              console.log("Killing message instance.");
              child.kill();
          }

           // Run the display with the new mesall-11-doctors.sage.ppm
          console.log('Calling led-matrix with all-11-doctors.ppm');
          child =  exec('sudo matrix/led-matrix -r 32 -c 4 -D 1 matirx/all-11-doctors.ppm');

       });

   thingShadows
      .on('delta', function(thingName, stateObject) {
         console.log('received delta on ' + thingName + ': ' +
            JSON.stringify(stateObject));
          // after you get the updated state call your command line function(s)
          // to render the text on the RGB LED board

          // Check for child state
          console.log("Kill check....");
          if (child){
              console.log("Killing message instance.");
              child.kill();
          }

          console.log('Calling text_to_ppm with: \"' + stateObject.state.message_1 + '\"');
          execSync('python matrix/text_to_ppm.py \"' + stateObject.state.message_1 + '\"');

          // Run the display with the new message.ppm
          console.log('Calling led-matrix with message.ppm');
          child =  exec('sudo matrix/led-matrix -r 32 -c 4 -D 1 matrix/message.ppm');


          // // Create the message.ppm
          // console.log('Calling text_to_ppm with: \"' + stateObject.state.message_1 + '\"');
          // spawnSync('python matrix/text_to_ppm.py \"' + stateObject.state.message_1 + '\"', function (error, out, stderr) {
          //    console.log(out);
          // });
          //
          // execSync('python matrix/text_to_ppm.py \"' + stateObject.state.message_1 + '\"');
          //
          // // Kill node and run this -- Run the display with the new message.ppm
          // console.log('Calling node aws-iot-device-sdk-js/pxl-echo.js')
          // execSync('node aws-iot-device-sdk-js/pxl-echo.js --thing-name PXL-CF2016 -f ~/.aws/certs');
          //
          // // Run the display with the new message.ppm
          // console.log('Calling led-matrix with message.ppm')
          // exec('sudo matrix/led-matrix -r 32 -c 4 -D 1 message.ppm', function (error, out, stderr) {
          //   console.log(out);
          // });
          //
          // execSync('sudo matrix/led-matrix -r 32 -c 4 -D 1 message.ppm')

          // thingShadows.update(thingName, {
          //    state: {
          //       reported: stateObject.state
          //    }
          // });
      });

   thingShadows
      .on('timeout', function(thingName, clientToken) {
         console.warn('timeout: ' + thingName + ', clientToken=' + clientToken);
      });
}

module.exports = cmdLineProcess;

if (require.main === module) {
   cmdLineProcess('connect to the AWS IoT service and perform thing shadow echo',
      process.argv.slice(2), processTest, ' ', true);
}
