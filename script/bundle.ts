import * as Bun from "bun"

let bundle = await Bun.build({
    entrypoints: ["./src/main.ts"],
    outdir: "./build",
    minify: false,
    //sourcemap: "external",
    plugins: [ /* ... */ ]
  })

if (!bundle.success) {
  console.log(bundle)
}

export {}