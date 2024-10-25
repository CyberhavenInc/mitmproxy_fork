from mitmproxy import addons
from mitmproxy import master
from mitmproxy import options
from mitmproxy.addons import intercept
from mitmproxy.addons import errorcheck
from mitmproxy.addons import keepserving
from mitmproxy.addons import readfile


class BackgroundMaster(master.Master):
    def __init__(self,options: options.Options, loop=None) -> None:
        super().__init__(options, event_loop=loop, with_termlog=False)
        self.addons.add(*addons.default_addons())
        self.addons.add(
            intercept.Intercept(),
            keepserving.KeepServing(),
            readfile.ReadFileStdin(),
            errorcheck.ErrorCheck(),
        )
