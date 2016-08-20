node {
   stage 'build'
   git 'https://github.com/XP2016India/Pitfalls-of-Continuous-Deployment.git'
   sh 'pip install -r requirements.txt'
   stage 'test'
   sh 'python -m unittest sample.test_services'
}
stage name: 'integration', concurrency: 1
node {
   sh 'sleep 30'
}
node {
   stage 'package'
   try {
    sh 'rm *.tar.gz'
   } catch(error) {}
   sh 'echo "build = $BUILD_NUMBER" > sample/config.py'
   sh 'tar -zcvf sample.tar.gz sample/'
   archive includes: '*.tar.gz'
}
stage name: 'staging', concurrency: 1
node {
    sh 'fab staging deploy'
}
timeout(time: 30, unit: 'SECONDS') {
    input 'Deploy to live?'
}
stage name: 'live', concurrency: 1
node {
    sh 'fab production deploy'
}
