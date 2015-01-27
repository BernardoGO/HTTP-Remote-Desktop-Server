import wx
from BaseHTTPServer import HTTPServer
import mimetypes
import urlparse
import gtk.gdk
from BaseHTTPServer import BaseHTTPRequestHandler

def take_ss():
    

    w = gtk.gdk.get_default_root_window()
    sz = w.get_size()
    print "The size of the window is %d x %d" % sz
    pb = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB,False,8,sz[0],sz[1])
    #return pb
    pb = pb.get_from_drawable(w,w.get_colormap(),0,0,0,0,sz[0],sz[1])
    
    if (pb != None):
        pb.save("screenshot.png","png")
        print "Screenshot saved to screenshot.png."
    else:
        print "Unable to get the screenshot."

def read(self, filename, getNpost):
    try:
        if len(filename) < 2:
            filename = "screenshot.png"
        filepath = filename
        #allow = pathManager.verify_all(filepath)
        #if allow == False:
        #    return messages.Forbidden
        take_ss()
        file_handler = open(filepath.replace("/", ""), 'rb')

        response = file_handler.read()
        #response = pythonCore.replaceAll(self, response, getNpost)
        return [200, response]
    except Exception as e:
        return [404, 'Not Found' + str(e)]


def do_GET(self):
    #execfile('takess.py')

    parsed_path = urlparse.urlparse(self.path)
    #sessionId = sessionManager.startSession(self)
    par = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    response = read(self, parsed_path.path, [par, None])
    self.send_response(response[0])
    #self.send_header('Set-Cookie', cookieHandler.WriteCookie(self, config.__SESSION_COOKIE_NAME__, sessionId))
    self.end_headers()
    self.wfile.write(response[1])
    return

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #pass
        do_GET(self)



server = HTTPServer(("127.0.0.1", 8010), requestHandler)

print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()


