# Open-source

## My projects

### Delta Client

[Delta Client](https://deltaclient.app) is a complete rewrite of the 'Minecraft: Java Edition' client. It is fully compatible with 'Minecraft: Java Edition' servers and is written in Swift. Due to a lot of optimisations and better design decisions, it is multiple times faster and more efficient than any other Minecraft client. The website contains more specific metrics.

### Swift Bundler

[Swift Bundler](https://github.com/stackotter/swift-bundler) is a modern tool for creating cross-platform Swift apps using Swift packages instead of Xcodeproj’s. It currently only supports macOS. iOS support in an experimental state. Windows and Linux support will be added in the future.

### SwiftCrossUI

[SwiftCrossUI](https://github.com/stackotter/swift-cross-ui) is a declarative cross-platform UI framework inspired by Apple's SwiftUI. Why not just use SwiftUI? Because it is built on top of Gtk and supports many more platforms than SwiftUI (which only supports Apple platforms). It is still in a very early stage of development.

### SwiftProtobufGen

[SwiftProtobufGen](https://github.com/stackotter/swift-protobuf-gen) is a tool for generating Protobuf message definitions from Swift structs. It can also generate the code required to convert to and from Protobuf messages. It is not yet in a usable state, but if there is enough interest I will continue working on it at some point.

### SwiftCSSParser

[SwiftCSSParser](https://github.com/stackotter/swift-css-parser) is a Swift package which provides a type-safe API for parsing, modifying and serializing CSS. It is built on top of the [c++ cssparser library](https://github.com/Sigil-Ebook/cssparser). I used it to create a page-content aware css minifier for my static static generator -- [Scute](https://github.com/stackotter/Scute) -- and it seems to be performing well.

### SwiftMixin

[SwiftMixin](https://github.com/stackotter/swift-mixin) is a highly experimental Swift package for replacing functions and methods dynamically at runtime. It only supports x86_64 and will probably break with every new Swift release. I plan on eventually writing an article about what I learnt from creating the package.

## Contributions to community projects

### FlyingFox

In 2022 I found two security vulnerabilities in [FlyingFox](https://github.com/swhitty/FlyingFox) -- a Swift HTTP implementation which takes advantage of Swift concurrency. [The first vulnerability](https://github.com/swhitty/FlyingFox/issues/24) was a path traversal vulnerability giving access to all of a server's files. And [the second vulnerability](https://github.com/swhitty/FlyingFox/issues/26) was a pointer arithmetic error in the socket implementation which could leak unintended memory to a user under certain conditions. Both of them have now been fixed.

### Parsley

In 2022 I brought [Parsley](https://github.com/loopwerk/Parsley) (a Swift wrapper of the cmark-gfm markdown parser) up-to-date with the latest version of cmark-gfm to mitigate the multiple vulnerabilities that it was exposed to. Most importantly, [the arbitrary code execution vulnerability in table parsing](https://github.com/github/cmark-gfm/security/advisories/GHSA-mc3g-88wq-6f4x). I also added support for custom markdown syntax extensions so that I could use it in my Swift-based static site generator -- [Scute](https://github.com/stackotter/Scute).

### TOMLKit

TOML is my favourite configuration file format and I think that [LebJe's TOMLKit](https://github.com/Lebje/TOMLKit) is a great step towards increasing adoption of TOML among Swift programmers. In 2022 I fixed a fatal parsing error that could occur when an array was provided in a place that TOMLKit expected a table. 


