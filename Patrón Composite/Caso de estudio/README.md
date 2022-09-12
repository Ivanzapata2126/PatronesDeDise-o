The base Component class declares common operations for both simple and complex objects of a composition.
Optionally, the base Component can declare an interface for setting and accessing a parent of the component in a tree structure. It can also provide some default implementation for these methods.

In some cases, it would be beneficial to define the child-management operations right in the base Component class. This way, you won't need to
expose any concrete component classes to the client code, even during the object tree assembly. The downside is that these methods will be empty for the leaf-level components.

You can provide a method that lets the client code figure out whether a component can bear children. The base Component may implement some default behavior or leave it to concrete classes (by declaring the method containing the behavior as "abstract"). The Leaf class represents the end objects of a composition. A leaf can't have any children. Usually, it's the Leaf objects that do the actual work, whereas Composite objects only delegate to their sub-components.

 The Composite class represents the complex components that may have children. Usually, the Composite objects delegate the actual work to their
 children and then "sum-up" the result. A composite object can add or remove other components (both simple or complex) to or from its child list. The Composite executes its primary logic in a particular way. It traverses recursively through all its children, collecting and summing
 their results. Since the composite's children pass these calls to their children and so forth, the whole object tree is traversed as a result.

The client code works with all of the components via the base interface. Thanks to the fact that the child-management operations are declared in the base Component class, the client code can work with any component, simple or complex, without depending on their concrete classes.