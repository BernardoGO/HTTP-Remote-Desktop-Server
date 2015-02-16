import wx
from BaseHTTPServer import HTTPServer
import mimetypes
import urlparse
import gtk.gdk
from BaseHTTPServer import BaseHTTPRequestHandler
import pyautogui

IP = "191.185.252.164"
PORT = 9010
SCR_X = 1600
SCR_Y = 900

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
            filename = "index.html"
        filepath = filename
        #allow = pathManager.verify_all(filepath)
        #if allow == False:
        #    return messages.Forbidden
        take_ss()
        file_handler = open(filepath.replace("/", ""), 'rb')

        response = file_handler.read()
        response = response.replace("[IP]", str(self.headers.getheader('host')).split(':')[0] ).replace("[PORT]", str(PORT) ).replace("[SCR_X]", str(SCR_X) ).replace("[SCR_Y]", str(SCR_Y) )
        #response = pythonCore.replaceAll(self, response, getNpost)
        return [200, response]
    except Exception as e:
        return [404, 'Not Found' + str(e)]

epoch = ""
keyevent = ""

def do_GET2(self):
    #execfile('takess.py')
    print self.path

    #print " add:"+ str(self.headers.getheader('host'))
    parsed_path = urlparse.urlparse(self.path)
    #sessionId = sessionManager.startSession(self)
    par = urlparse.parse_qs(urlparse.urlparse(self.path).query)
    set = False
    global epoch
    global keyevent
    try:
        #print par['mouse_x']
        #print par['mouse_y']
        if epoch != par['epoch']:
            set = True
    except:
        pass

    try:
        if set == True:
            #pyautogui.moveTo(int(par['mouse_x'][0]), int(par['mouse_y'][0]))
            pyautogui.click(int(par['mouse_x'][0]), int(par['mouse_y'][0]))
            epoch = par['epoch']
    except:
        pass

    try:
        if keyevent != par['_']:
            #pyautogui.moveTo(int(par['mouse_x'][0]), int(par['mouse_y'][0]))
            pyautogui.keyDown(par['key'][0])
            keyevent = par['_']
    except:
        pass


    response = read(self, parsed_path.path, [par, None])
    self.send_response(response[0])
    #self.send_header('Set-Cookie', cookieHandler.WriteCookie(self, config.__SESSION_COOKIE_NAME__, sessionId))
    self.end_headers()
    self.wfile.write(response[1])
    return

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        #pass
        do_GET2(self)



server = HTTPServer(("", PORT), requestHandler)

print 'Starting server, use <Ctrl-C> to stop'
server.serve_forever()


