class Directive extends Injectable {
  static $type = 'directive';
  static module = '';
  static dependencies = [];
  static tagName = '';


  static register(directive) {
    const injected = directive.dependencies.slice(0);

    injected.push(function() {
      const instance = Object.create(directive.prototype);
      directive.apply(instance, arguments);

      if (instance.link) {
        instance.link = instance.link.bind(instance);
      }

      return instance;
    });

    angular
      .module(directive.module)
      .directive(directive.tagName, injected);
  }
}
