#include <iostream>

class Media {
public:
    virtual ~Media() {}
    const std::string& getFilename() const { return filename; }
    virtual void play() const = 0;
    virtual void pause() const = 0;
protected:
    Media(const std::string &_filename) : filename(_filename) {}
private:
    std::string filename;
};

class AudioPlayer : virtual public Media {
public:
    AudioPlayer(const std::string &_filename) : Media(_filename) {}
    virtual void play() const override {
        std::cout << "AudioPlayer: playing: " << getFilename() << std::endl;
    }
    virtual void pause() const override {
        std::cout << "AudioPlayer: paused: " << getFilename() << std::endl;
    }
    void setVolume(unsigned int newVolume) { volume = newVolume; }
private:
    unsigned int volume = 100;
};

class VideoPlayer : virtual public Media {
public:
    VideoPlayer(const std::string &_filename) : Media(_filename) {}
    virtual void play() const override {
        std::cout << "VideoPlayer: playing: " << getFilename() << std::endl;
    }
    virtual void pause() const override {
        std::cout << "VideoPlayer: paused: " << getFilename() << std::endl;
    }
    virtual void setBrightness(int &newBrightness) { brightness = newBrightness; }
private:
    int brightness = 100;
};

class AVPlayer : public AudioPlayer, public VideoPlayer {
public:
    AVPlayer(const std::string &_filename) : AudioPlayer(_filename), VideoPlayer(_filename), Media(_filename) {}
    virtual void play() const override {
        std::cout << "AVPlayer: synchronizing a/v: " << getFilename() << std::endl;
        AudioPlayer::play();
        VideoPlayer::play();
    }
    virtual void pause() const override {
        std::cout << "AVPlayer: pausing: " << getFilename() << std::endl;
        AudioPlayer::pause();
        VideoPlayer::pause();
    }
};





int main() {
    AVPlayer av("Film1");
    av.play();
    std::cout << std::endl;
    av.pause();

    return 0;
}