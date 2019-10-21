/**
 * Loop audio files infinitely with this minimalist command-line application 
 */

import java.io.BufferedInputStream;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.IOException;
import java.io.FileNotFoundException;

import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.LineUnavailableException;
import javax.sound.sampled.SourceDataLine;
import javax.sound.sampled.DataLine;
import javax.sound.sampled.FloatControl;
import javax.sound.sampled.Control;
import javax.sound.sampled.UnsupportedAudioFileException;


/**
 * Controls :
 * Master Gain with current value: 0.0 dB (range: -80.0 - 6.0206)
 * Mute Control with current value: False
 * Balance with current value: 0.0  (range: -1.0 - 1.0)
 * Pan with current value: 0.0  (range: -1.0 - 1.0)
 */
public class LoopAudioPlayer {
    private static final int BUFFER_SIZE = 128000;

    // All outputs provided by the software
    private static final String USAGE = "LoopAudioPlayer: usage:\n\tjava LoopAudioPlayer <file>";
    private static final String ERROR_MESSAGE_RESETTING_NOT_SUPPORTED = "Resetting an audio file is not supported.";
    private static final String ERROR_MESSAGE_UNCALCULABLE_INPUT_LENGTH = "Can't compute the length of the audio stream.";
    private static final String ERROR_MESSAGE_FILE_NOT_FOUND = "Can't find the audio file.";
    private static final String ERROR_MESSAGE_FILE_NOT_SUPPORTED = "This audio type is currently not supported.";
    private static final String ERROR_MESSAGE_LOADING_STREAM = "Error while reading the audio stream.";
    private static final String ERROR_MESSAGE_LINE_UNAVAILABLE = "Audio line currently unavailable.";
    private static final String ERROR_MESSAGE_INPUT_LENGTH_TOO_LONG = "The length of the stream exceeds 2^31 bytes, cannot properly reset stream.";
    private static final String ERROR_MESSAGE_RESETTING_SOUND = "Can't properly reset the sound.";
    private static final String ERROR_MESSAGE_PLAYING_SOUND = "Input error while playing the sound";

    // All error code provided by the software
    private static final int EXIT_SUCCESS = 0;
    private static final int ERROR_CODE_WRONG_NUMBER_OF_ARGUMENTS = 1;
    private static final int ERROR_CODE_RESETTING_NOT_SUPPORTED = 2;
    private static final int ERROR_CODE_UNCALCULABLE_INPUT_LENGTH = 3;
    private static final int ERROR_CODE_FILE_NOT_FOUND = 4;
    private static final int ERROR_CODE_FILE_NOT_SUPPORTED = 5;
    private static final int ERROR_CODE_LOADING_STREAM = 6;
    private static final int ERROR_CODE_LINE_UNAVAILABLE = 7;
    private static final int ERROR_CODE_INPUT_LENGTH_TOO_LONG = 8;
    private static final int ERROR_CODE_RESETTING_SOUND = 9;
    private static final int ERROR_CODE_PLAYING_SOUND = 10;

    // Variable needed by the class
    private static String filepath;
    
    // Variables used by the class
    private static FloatControl volumeControl;
    private static AudioInputStream audioInputStream;
    private static SourceDataLine sourceDataLine;


    public static void main(String[] args) {
        parseArguments(args);
        loadInputStream(filepath);
        loadSourceDataLine();
        loopSound(audioInputStream, sourceDataLine, BUFFER_SIZE);
    }


    /**
     * Parse the arguments provided by the user.
     * If the user has passed more or less than 1 argument, the software will
     * terminate with an appropriate error message and error code.
     */
    private static void parseArguments(String[] args) {
        if (args.length != 1) {
            System.out.println(USAGE);
            System.exit(ERROR_CODE_WRONG_NUMBER_OF_ARGUMENTS);
        }

        filepath = args[0];
    }


    /**
     * Return the audio content in form of a stream located at filepath.
     */
    private static void loadInputStream(String filepath) {
        try {
            InputStream fileInputStream = new FileInputStream(filepath);
            InputStream bufferedInputStream = new BufferedInputStream(fileInputStream);

            audioInputStream = AudioSystem.getAudioInputStream(bufferedInputStream);
            if (! audioInputStream.markSupported()) {
                System.out.println(ERROR_MESSAGE_RESETTING_NOT_SUPPORTED);
                System.exit(ERROR_CODE_RESETTING_NOT_SUPPORTED);
            }
            if (audioInputStream.getFrameLength() == AudioSystem.NOT_SPECIFIED ||
                audioInputStream.getFormat().getFrameSize() == AudioSystem.NOT_SPECIFIED) {
                System.out.println(ERROR_MESSAGE_UNCALCULABLE_INPUT_LENGTH);
                System.exit(ERROR_CODE_UNCALCULABLE_INPUT_LENGTH);
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
            System.out.println(ERROR_MESSAGE_FILE_NOT_FOUND);
            System.exit(ERROR_CODE_FILE_NOT_FOUND);
        } catch (UnsupportedAudioFileException e) {
            e.printStackTrace();
            System.out.println(ERROR_MESSAGE_FILE_NOT_SUPPORTED);
            System.exit(ERROR_CODE_FILE_NOT_SUPPORTED);
        } catch (IOException e) {
            e.printStackTrace();
            System.out.println(ERROR_MESSAGE_LOADING_STREAM);
            System.exit(ERROR_CODE_LOADING_STREAM);            
        }
    }


    /**
     * Open a SourceDataLine and load the resources needed.
     */
    private static void loadSourceDataLine() {
        DataLine.Info info = new DataLine.Info(SourceDataLine.class, audioInputStream.getFormat());
        try {
            sourceDataLine = (SourceDataLine) AudioSystem.getLine(info);

            /* The line has been opened, but it is not yet ready to receive
               audio data. We have to open the line to load the resources
               needed. */
            sourceDataLine.open(audioInputStream.getFormat());
        } catch (LineUnavailableException e) {
            e.printStackTrace();
            System.out.println(ERROR_MESSAGE_LINE_UNAVAILABLE);
            System.exit(ERROR_CODE_LINE_UNAVAILABLE);
        }

        // Initialize the volume controler
        System.out.println("CONTROLERS:");
        for (Control c : sourceDataLine.getControls()) {
            System.out.println(c);
        }
        if (sourceDataLine.isControlSupported(FloatControl.Type.MASTER_GAIN)) {
            volumeControl = (FloatControl) sourceDataLine.getControl(FloatControl.Type.MASTER_GAIN);
        }
    }


    /**
     * Check if the stream is readable and of an appropriate size, then return
     * its size in bytes.
     */
    private static int computeStreamLength(AudioInputStream audioInputStream) {
        long streamLength = audioInputStream.getFrameLength() * audioInputStream.getFormat().getFrameSize();
        if (streamLength > Integer.MAX_VALUE) {
            System.out.println(ERROR_MESSAGE_INPUT_LENGTH_TOO_LONG);
            System.exit(ERROR_CODE_INPUT_LENGTH_TOO_LONG);
        }
        return (int) streamLength;
    }


    private static void loopSound(AudioInputStream audioInputStream,
                                  SourceDataLine sourceDataLine,
                                  int bufferSize) {
        int streamLength = computeStreamLength(audioInputStream);
        byte[] dataBuffer = new byte[bufferSize];

        sourceDataLine.start();
        while (true) {
            try {
                playSound(audioInputStream, sourceDataLine, streamLength,
                          dataBuffer);
                audioInputStream.reset();
            } catch (IOException e) {
                e.printStackTrace();
                System.out.println(ERROR_MESSAGE_RESETTING_SOUND);
                System.exit(ERROR_CODE_RESETTING_SOUND);
            }
        }
    }


    private static void playSound(AudioInputStream audioInputStream,
                                  SourceDataLine sourceDataLine,
                                  int streamLength,
                                  byte[] dataBuffer) {
        audioInputStream.mark(streamLength);
        int bytesRead = 0;
        while (bytesRead != -1) {
            try {
                bytesRead = audioInputStream.read(dataBuffer, 0,
                                                  dataBuffer.length);
                if (bytesRead >= 0) {
                    sourceDataLine.write(dataBuffer, 0, bytesRead);
                }
            } catch (IOException e) {
                e.printStackTrace();
                System.out.println(ERROR_MESSAGE_PLAYING_SOUND);
                System.exit(ERROR_CODE_PLAYING_SOUND);
            }
        }
    }
}
