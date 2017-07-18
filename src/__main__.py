from douban import get_movie
import sys
import traceback

def main():
    """Main entry point"""
    try:
        if len(sys.argv) >= 2:
            get_movie(sys.argv[1])
        else:
            print 'try command "douban movie_name"'
    except Exception as e:
        print 'exception', e
        traceback.print_exc()
        pass
