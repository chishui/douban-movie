from douban import *
from view import run
import sys
import traceback
import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("movie_name", help="set the name of movie you want to get")
    parser.add_argument("-l", "--listall", help="show possible movie list",
        action="store_true")

    return parser.parse_args()

def main():
    """Main entry point"""
    try:
        args = get_args()
        if args.listall:
            movies = search(args.movie_name)
            movie = run(movies)
            if movie:
                parse(movie)
        else:
            get_movie(args.movie_name)
    except Exception as e:
        print 'exception', e
        traceback.print_exc()
        pass
